#!/usr/bin/env python3
"""
Sync video titles and descriptions from conference session YAML to YouTube.

Two phases:

1. ``match`` — fetch the authenticated channel's uploads, fuzzy-match each
   upload against a session in the YAML by title, and write the chosen
   ``youtubeId`` back into the YAML for review.

2. ``sync`` (default) — for each session with a ``youtubeId``, build a title
   and description from the YAML and update the YouTube video.

Setup:
    1. Create an OAuth client (Desktop app) in Google Cloud Console for a
       project with the YouTube Data API v3 enabled.
    2. Download the client secrets JSON to ``~/.config/wtd/youtube_client_secret.json``
       (or pass ``--client-secrets``).
    3. The video owner's Google account must authorize the app on first run;
       a refresh token is cached at ``~/.config/wtd/youtube_token.json``.

Usage:
    # Match channel uploads to sessions and write youtubeId back to the YAML
    uv run python docs/_scripts/sync-youtube-metadata.py match --dry-run
    uv run python docs/_scripts/sync-youtube-metadata.py match

    # Push titles + descriptions to YouTube
    uv run python docs/_scripts/sync-youtube-metadata.py sync --dry-run
    uv run python docs/_scripts/sync-youtube-metadata.py sync

Requires (install ad-hoc, not part of project deps):
    uv pip install google-auth google-auth-oauthlib google-api-python-client PyYAML
"""

import argparse
import difflib
import html
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SESSIONS = REPO_ROOT / "docs" / "_data" / "portland-2026-sessions.yaml"
DEFAULT_SCHEDULE = REPO_ROOT / "docs" / "_data" / "portland-2026-schedule.yaml"
DEFAULT_LT_YAML = REPO_ROOT / "docs" / "_data" / "portland-2026-lightning-talks.yaml"
DEFAULT_CONF_URL = "https://www.writethedocs.org/conf/portland/2026/"
DEFAULT_PLAYLIST_TITLE = "Write the Docs Portland 2026"
DEFAULT_PLAYLIST_DESCRIPTION = (
    "Talks from Write the Docs Portland 2026, the annual conference for everyone "
    "who writes the docs. https://www.writethedocs.org/conf/portland/2026/"
)

CONFIG_DIR = Path(os.environ.get("WTD_CONFIG_DIR", Path.home() / ".config" / "wtd"))
DEFAULT_CLIENT_SECRETS = CONFIG_DIR / "youtube_client_secret.json"
DEFAULT_TOKEN_FILE = CONFIG_DIR / "youtube_token.json"

SCOPES = ["https://www.googleapis.com/auth/youtube"]

# YouTube limits: title <= 100 chars, description <= 5000 chars.
TITLE_MAX = 100
DESCRIPTION_MAX = 5000


class _HTMLToText(HTMLParser):
    """Minimal HTML-to-text converter for session abstracts."""

    BLOCK_TAGS = {"p", "div", "br", "li"}
    LIST_TAGS = {"ul", "ol"}

    def __init__(self):
        super().__init__()
        self._parts = []
        self._in_li = False

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self._parts.append("\n- ")
            self._in_li = True
        elif tag in self.BLOCK_TAGS:
            self._parts.append("\n\n")
        elif tag in self.LIST_TAGS:
            self._parts.append("\n")

    def handle_endtag(self, tag):
        if tag == "li":
            self._in_li = False
        elif tag in self.BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data):
        self._parts.append(data)

    def text(self):
        joined = "".join(self._parts)
        joined = html.unescape(joined)
        # Collapse runs of >2 newlines and trim trailing whitespace per line.
        joined = re.sub(r"[ \t]+\n", "\n", joined)
        joined = re.sub(r"\n{3,}", "\n\n", joined)
        return joined.strip()


def html_to_text(html_str):
    if not html_str:
        return ""
    parser = _HTMLToText()
    parser.feed(html_str)
    return parser.text()


def speaker_names(session):
    names = [s.get("name", "").strip() for s in session.get("speakers", [])]
    return [n for n in names if n]


def build_title(session):
    title = session["title"].strip()
    names = speaker_names(session)
    if names:
        suffix = " - " + ", ".join(names)
    else:
        suffix = ""

    full = f"{title}{suffix}"
    if len(full) <= TITLE_MAX:
        return full

    # Title alone fits — drop speakers.
    if len(title) <= TITLE_MAX:
        return title

    # Last resort: truncate.
    return title[: TITLE_MAX - 1].rstrip() + "…"


def build_description(session, conf_url):
    lines = []

    names = speaker_names(session)
    if names:
        lines.append("Speaker{}: {}".format("s" if len(names) > 1 else "", ", ".join(names)))
        lines.append("")

    abstract = html_to_text(session.get("abstract", ""))
    if abstract:
        lines.append(abstract)
        lines.append("")

    speaker_links = []
    for speaker in session.get("speakers", []):
        name = speaker.get("name", "").strip()
        website = (speaker.get("website") or "").strip()
        if name and website:
            speaker_links.append(f"  {name}: {website}")
    if speaker_links:
        lines.append("About the speaker{}:".format("s" if len(speaker_links) > 1 else ""))
        lines.extend(speaker_links)
        lines.append("")

    series = session.get("series", "Write the Docs")
    year = session.get("year", "")
    recorded = f"Recorded at {series} {year}.".strip().rstrip(".") + "."
    lines.append(recorded)
    lines.append(conf_url)

    description = "\n".join(lines).strip()
    if len(description) > DESCRIPTION_MAX:
        description = description[: DESCRIPTION_MAX - 1].rstrip() + "…"
    return description


def load_sessions(path):
    with open(path, encoding="utf-8") as fp:
        return yaml.safe_load(fp) or []


def get_youtube_client(client_secrets, token_file):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    creds = None
    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    elif not creds or not creds.valid:
        if not client_secrets.exists():
            raise SystemExit(
                f"Missing OAuth client secrets at {client_secrets}. "
                "Create an OAuth Desktop client in Google Cloud Console and place the JSON there."
            )
        flow = InstalledAppFlow.from_client_secrets_file(str(client_secrets), SCOPES)
        creds = flow.run_local_server(port=0)
        token_file.parent.mkdir(parents=True, exist_ok=True)
        token_file.write_text(creds.to_json())

    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def fetch_existing(youtube, video_ids):
    existing = {}
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        resp = youtube.videos().list(part="snippet", id=",".join(batch)).execute()
        for item in resp.get("items", []):
            existing[item["id"]] = item["snippet"]
    return existing


def update_video(youtube, video_id, snippet, title, description):
    new_snippet = dict(snippet)
    new_snippet["title"] = title
    new_snippet["description"] = description
    # categoryId is required by the API on update; preserve existing or default to 27 (Education).
    new_snippet.setdefault("categoryId", "27")
    youtube.videos().update(
        part="snippet",
        body={"id": video_id, "snippet": new_snippet},
    ).execute()


def resolve_channel(youtube, channel):
    """Resolve a channel handle, URL, or ID into a channel ID."""
    s = channel.strip()
    if s.startswith("http"):
        m = re.search(r"(?:channel/|@)([A-Za-z0-9_\-]+)", s)
        if not m:
            raise SystemExit(f"Could not parse channel URL: {channel}")
        s = ("@" + m.group(1)) if "@" in channel else m.group(1)

    if s.startswith("UC") and len(s) >= 20:
        return s

    handle = s.lstrip("@")
    resp = youtube.channels().list(part="id", forHandle="@" + handle).execute()
    items = resp.get("items", [])
    if not items:
        raise SystemExit(f"No channel found for handle @{handle}")
    return items[0]["id"]


def fetch_channel_uploads(youtube, channel=None):
    """Return [(video_id, title), ...] for every upload on a channel.

    If ``channel`` is given (ID, handle, or URL), uploads come from that channel
    (public/unlisted that the authorized account can see). Otherwise the
    authenticated account's own uploads.
    """
    if channel:
        channel_id = resolve_channel(youtube, channel)
        chan = youtube.channels().list(part="contentDetails", id=channel_id).execute()
    else:
        chan = youtube.channels().list(part="contentDetails", mine=True).execute()
    items = chan.get("items", [])
    if not items:
        raise SystemExit("No channel found for the given selector.")
    uploads_playlist = items[0]["contentDetails"]["relatedPlaylists"]["uploads"]

    uploads = []
    page_token = None
    while True:
        resp = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=uploads_playlist,
            maxResults=50,
            pageToken=page_token,
        ).execute()
        for item in resp.get("items", []):
            uploads.append((
                item["contentDetails"]["videoId"],
                item["snippet"]["title"],
            ))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return uploads


def _normalize_for_match(text):
    text = text.lower()
    text = re.sub(r"\[[^\]]*\]", " ", text)  # drop bracketed prefixes like "[Remote talk]"
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return " ".join(text.split())


def _alnum_lower(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


def _upload_alnum(title):
    """Lowercase alnum-only, with any leading date like '2026 05 05' stripped."""
    stripped = re.sub(r"^\s*\d{4}\s+\d{1,2}\s+\d{1,2}\s+", "", title)
    return _alnum_lower(stripped)


def _session_speaker_keys(session):
    """Return alnum-lower keys for each speaker on a session (e.g. 'ethanpalm')."""
    keys = []
    for s in session.get("speakers", []):
        name = s.get("name", "").strip()
        if name:
            keys.append(_alnum_lower(name))
    return keys


def _score_pair(session, upload_title):
    """Score how well an upload title matches a session.

    Tries three signals, in order:
      1. Speaker full name (alnum-collapsed) is a substring of the upload.
      2. Speaker full name is *near* a token in the upload (handles typos).
      3. Talk-title similarity (the original strategy).
    """
    upload_alnum = _upload_alnum(upload_title)
    keys = _session_speaker_keys(session)

    for key in keys:
        if len(key) >= 6 and key in upload_alnum:
            return 0.95

    # Fuzzy: compare each speaker key against the alnum upload string. Useful
    # when upload titles contain typos (e.g. "AlieenMary" vs "AileenMary").
    best_fuzzy = 0.0
    for key in keys:
        if len(key) < 6:
            continue
        ratio = difflib.SequenceMatcher(None, key, upload_alnum).ratio()
        # Boost if upload is mostly just the speaker name with a short date prefix.
        if len(upload_alnum) <= len(key) + 4:
            ratio = max(ratio, difflib.SequenceMatcher(None, key, upload_alnum[-len(key) - 2:]).ratio())
        best_fuzzy = max(best_fuzzy, ratio)
    if best_fuzzy >= 0.85:
        return 0.90

    return difflib.SequenceMatcher(
        None, _normalize_for_match(session["title"]), _normalize_for_match(upload_title)
    ).ratio()


def match_uploads_to_sessions(uploads, sessions, threshold=0.55):
    """Greedy best-pair matching between uploads and sessions.

    Returns (matches, unmatched_sessions, unmatched_uploads) where matches is a list of
    (session_index, video_id, video_title, score).
    """
    scored = []
    for s_idx, session in enumerate(sessions):
        for vid, vtitle in uploads:
            scored.append((_score_pair(session, vtitle), s_idx, vid, vtitle))
    scored.sort(reverse=True)

    used_sessions = set()
    used_videos = set()
    matches = []
    for score, s_idx, vid, vtitle in scored:
        if score < threshold:
            break
        if s_idx in used_sessions or vid in used_videos:
            continue
        used_sessions.add(s_idx)
        used_videos.add(vid)
        matches.append((s_idx, vid, vtitle, score))

    unmatched_sessions = [i for i in range(len(sessions)) if i not in used_sessions]
    unmatched_uploads = [(vid, t) for vid, t in uploads if vid not in used_videos]
    return matches, unmatched_sessions, unmatched_uploads


def write_youtube_ids(sessions_path, matches, sessions):
    """Insert or replace ``youtubeId:`` lines in the YAML via text patching.

    Avoids the formatting churn of a full YAML round-trip (which would re-wrap
    long abstract strings). For each matched session we locate its top-level
    list entry by ``slug:`` and either replace the existing ``youtubeId:`` line
    or append one at the end of that entry.
    """
    with open(sessions_path, encoding="utf-8") as fp:
        text = fp.read()
    lines = text.splitlines(keepends=True)

    # Find start-of-entry line indexes (lines starting with "- title:").
    entry_starts = [i for i, ln in enumerate(lines) if ln.startswith("- title:")]
    entry_starts.append(len(lines))  # sentinel for last entry end

    if len(entry_starts) - 1 != len(sessions):
        raise SystemExit(
            f"Entry count mismatch: {len(entry_starts) - 1} YAML entries vs {len(sessions)} parsed sessions"
        )

    # Build slug -> session_index map (slugs are unique in these files).
    slug_to_idx = {sessions[i].get("slug"): i for i in range(len(sessions))}

    # Index entry blocks by slug.
    entry_by_slug = {}
    for n in range(len(entry_starts) - 1):
        start, end = entry_starts[n], entry_starts[n + 1]
        for j in range(start, end):
            m = re.match(r"  slug:\s*(\S+)", lines[j])
            if m:
                entry_by_slug[m.group(1)] = (start, end)
                break

    # Apply edits from bottom up so indexes stay valid.
    edits = []
    for s_idx, vid, _vtitle, _score in matches:
        slug = sessions[s_idx].get("slug")
        if slug not in entry_by_slug:
            print(f"  WARN: could not locate entry for slug {slug!r}; skipping")
            continue
        start, end = entry_by_slug[slug]
        edits.append((start, end, slug, vid))
    edits.sort(reverse=True)

    new_line_for = lambda v: f"  youtubeId: {v}\n"

    for start, end, _slug, vid in edits:
        # Look for an existing youtubeId line in this entry.
        replaced = False
        for j in range(start, end):
            if re.match(r"  youtubeId:\s", lines[j]):
                lines[j] = new_line_for(vid)
                replaced = True
                break
        if not replaced:
            # Append immediately before the next entry (preserving any trailing whitespace).
            insert_at = end
            while insert_at > start and lines[insert_at - 1].strip() == "":
                insert_at -= 1
            lines.insert(insert_at, new_line_for(vid))

    with open(sessions_path, "w", encoding="utf-8") as fp:
        fp.writelines(lines)


def cmd_match(args):
    sessions = load_sessions(args.sessions)
    if not sessions:
        print(f"No sessions found in {args.sessions}", file=sys.stderr)
        return 1

    youtube = get_youtube_client(args.client_secrets, args.token_file)
    uploads = fetch_channel_uploads(youtube, channel=args.channel)
    label = args.channel or "authenticated channel"
    print(f"{label} has {len(uploads)} uploads; YAML has {len(sessions)} sessions")

    matches, unmatched_s, unmatched_v = match_uploads_to_sessions(
        uploads, sessions, threshold=args.threshold,
    )

    print(f"\nMatched {len(matches)} session(s):")
    for s_idx, vid, vtitle, score in matches:
        existing = sessions[s_idx].get("youtubeId")
        marker = " (already set)" if existing == vid else (f" (was {existing})" if existing else "")
        print(f"  {score:.2f}  {vid}  {vtitle!r}")
        print(f"         <- {sessions[s_idx]['title']!r}{marker}")

    if unmatched_s:
        print(f"\nUnmatched sessions ({len(unmatched_s)}):")
        for i in unmatched_s:
            print(f"  - {sessions[i]['title']}")
    if unmatched_v:
        print(f"\nUnmatched uploads ({len(unmatched_v)}):")
        for vid, t in unmatched_v:
            print(f"  - {vid}  {t}")

    if args.dry_run:
        print("\nDry run: YAML not modified.")
        return 0

    write_youtube_ids(args.sessions, matches, sessions)
    print(f"\nWrote {len(matches)} youtubeId value(s) to {args.sessions}")
    return 0


def _format_speaker(speaker):
    name = speaker.get("name", "").strip()
    pronouns = (speaker.get("pronouns") or "").strip()
    return f"{name} ({pronouns})" if pronouns else name


def build_lt_title(day, series, year):
    return f"{day['name']} - {series} {year}"


def build_lt_description(day, lt_data):
    series = lt_data.get("series", "Write the Docs")
    year = lt_data.get("year", "")
    conf_url = lt_data.get("conf_url", DEFAULT_CONF_URL)
    coordinator = lt_data.get("coordinator", {})
    sponsor = day.get("sponsor") or {}

    lines = [f"{day['name']} at {series} {year}.".strip()]

    if sponsor.get("name"):
        sponsor_line = f"Sponsored by {sponsor['name']}"
        if sponsor.get("url"):
            sponsor_line += f" ({sponsor['url']})"
        sponsor_line += "."
        lines.append(sponsor_line)
    lines.append("")

    lines.append("Talks (in order of appearance):")
    lines.append("")
    for idx, talk in enumerate(day.get("talks", []), start=1):
        title = talk.get("title", "").strip()
        subtitle = (talk.get("subtitle") or "").strip()
        header = f"{idx}. {title}"
        if subtitle:
            header += f" — {subtitle}"
        lines.append(header)
        speaker = talk.get("speaker") or {}
        speaker_str = _format_speaker(speaker)
        if speaker_str:
            lines.append(f"   {speaker_str}")
        lines.append("")

    if coordinator.get("name"):
        role = (coordinator.get("role") or "Lightning Talks Coordinator").strip()
        lines.append(f"{role}: {_format_speaker(coordinator)}")
        lines.append("")

    lines.append(f"Recorded at {series} {year}.".rstrip(". ") + ".")
    lines.append(conf_url)

    description = "\n".join(lines).strip()
    if len(description) > DESCRIPTION_MAX:
        description = description[: DESCRIPTION_MAX - 1].rstrip() + "…"
    return description


def cmd_lt(args):
    with open(args.lt_yaml, encoding="utf-8") as fp:
        lt_data = yaml.safe_load(fp) or {}

    series = lt_data.get("series", "Write the Docs")
    year = lt_data.get("year", "")

    candidates = []
    for day in lt_data.get("days", []):
        yt_id = day.get("youtubeId")
        if not yt_id:
            print(f"  SKIP {day.get('name', '?')}: no youtubeId in YAML")
            continue
        title = build_lt_title(day, series, year)
        description = build_lt_description(day, lt_data)
        candidates.append((yt_id, day, title, description))

    if not candidates:
        print(f"No LT days with youtubeId in {args.lt_yaml}", file=sys.stderr)
        return 0

    print(f"Found {len(candidates)} lightning-talk day(s) to sync")

    if args.dry_run:
        for yt_id, day, title, description in candidates:
            print(f"\n--- https://www.youtube.com/watch?v={yt_id} ---")
            print(f"Title ({len(title)} chars): {title}")
            print(f"Description ({len(description)} chars):")
            print(description)
        return 0

    youtube = get_youtube_client(args.client_secrets, args.token_file)
    existing = fetch_existing(youtube, [yid for yid, _d, _t, _desc in candidates])

    updated = skipped = failed = 0
    for yt_id, day, title, description in candidates:
        snippet = existing.get(yt_id)
        if snippet is None:
            print(f"  SKIP {yt_id}: not found on YouTube (or not owned by authorized account)")
            skipped += 1
            continue
        if snippet.get("title") == title and snippet.get("description") == description:
            print(f"  SKIP {yt_id}: already in sync")
            skipped += 1
            continue
        try:
            update_video(youtube, yt_id, snippet, title, description)
            print(f"  OK   {yt_id}: {title}")
            updated += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL {yt_id}: {exc}")
            failed += 1

    print(f"\nUpdated {updated}, skipped {skipped}, failed {failed}")
    return 1 if failed else 0


def build_playlist_order(schedule_path, sessions_path, lt_yaml_path):
    """Return a list of (video_id, label) in conference-schedule order.

    Walks ``talks_day1`` then ``talks_day2`` in the schedule YAML. Each entry
    with a ``slug`` is looked up in the sessions YAML for its ``youtubeId``.
    Entries whose ``title`` contains "Lightning Talks" pull the matching day's
    video from the LT YAML.
    """
    with open(schedule_path, encoding="utf-8") as fp:
        schedule = yaml.safe_load(fp) or {}
    with open(sessions_path, encoding="utf-8") as fp:
        sessions = yaml.safe_load(fp) or []
    with open(lt_yaml_path, encoding="utf-8") as fp:
        lt_data = yaml.safe_load(fp) or {}

    slug_to_session = {s.get("slug"): s for s in sessions if s.get("slug")}
    lt_days = lt_data.get("days", [])

    order = []
    for day_key, lt_day in (("talks_day1", lt_days[0] if len(lt_days) > 0 else None),
                            ("talks_day2", lt_days[1] if len(lt_days) > 1 else None)):
        for item in schedule.get(day_key, []) or []:
            slug = item.get("slug")
            title = item.get("title", "") or ""
            if slug:
                session = slug_to_session.get(slug)
                if not session:
                    print(f"  WARN: schedule slug {slug!r} not found in sessions; skipping")
                    continue
                vid = session.get("youtubeId")
                if not vid:
                    print(f"  WARN: session {slug!r} has no youtubeId; skipping")
                    continue
                order.append((vid, session.get("title", slug)))
            elif "Lightning Talks" in title and lt_day and lt_day.get("youtubeId"):
                order.append((lt_day["youtubeId"], lt_day.get("name", "Lightning Talks")))

    return order


def find_playlist_by_title(youtube, title):
    page_token = None
    while True:
        resp = youtube.playlists().list(
            part="snippet,contentDetails,status",
            mine=True,
            maxResults=50,
            pageToken=page_token,
        ).execute()
        for item in resp.get("items", []):
            if item["snippet"]["title"] == title:
                return item
        page_token = resp.get("nextPageToken")
        if not page_token:
            return None


def fetch_playlist_items(youtube, playlist_id):
    """Return [{id, videoId, position, title}, ...] for items in this playlist."""
    items = []
    page_token = None
    while True:
        resp = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=page_token,
        ).execute()
        for item in resp.get("items", []):
            items.append({
                "id": item["id"],
                "videoId": item["contentDetails"]["videoId"],
                "position": item["snippet"]["position"],
                "title": item["snippet"]["title"],
            })
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    items.sort(key=lambda x: x["position"])
    return items


def cmd_playlist(args):
    desired = build_playlist_order(args.schedule, args.sessions, args.lt_yaml)
    if not desired:
        print("No videos resolved from schedule + sessions + LT YAML.", file=sys.stderr)
        return 1

    print(f"Desired playlist order ({len(desired)} videos):")
    for i, (vid, label) in enumerate(desired, start=1):
        print(f"  {i:2d}. {vid}  {label}")

    if args.dry_run and not args.create_only_if_dry_run:
        # In dry-run we still authenticate (so we can show what's there), unless --no-auth.
        if args.no_auth:
            print("\n(--no-auth) Skipping YouTube state lookup.")
            return 0

    youtube = get_youtube_client(args.client_secrets, args.token_file)
    playlist = find_playlist_by_title(youtube, args.title)

    if playlist is None:
        print(f"\nPlaylist {args.title!r} does not exist on the authenticated channel.")
        if args.dry_run:
            print("Dry run: would create it and add the videos above in order.")
            return 0
        resp = youtube.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": args.title,
                    "description": args.description,
                },
                "status": {"privacyStatus": args.privacy},
            },
        ).execute()
        playlist_id = resp["id"]
        print(f"Created playlist {playlist_id} ({args.privacy}).")
        current = []
    else:
        playlist_id = playlist["id"]
        print(f"\nFound existing playlist {playlist_id}.")
        current = fetch_playlist_items(youtube, playlist_id)
        print(f"Playlist currently has {len(current)} items.")

    current_by_video = {item["videoId"]: item for item in current}
    desired_ids = [vid for vid, _ in desired]

    plan_add = [(idx, vid, label) for idx, (vid, label) in enumerate(desired)
                if vid not in current_by_video]
    plan_reorder = []
    if args.reorder:
        for idx, (vid, _label) in enumerate(desired):
            item = current_by_video.get(vid)
            if item and item["position"] != idx:
                plan_reorder.append((idx, vid, item))
    extras = [item for item in current if item["videoId"] not in set(desired_ids)]
    plan_remove = extras if args.remove_extras else []

    print("\nPlan:")
    print(f"  add:     {len(plan_add)}")
    print(f"  reorder: {len(plan_reorder)}")
    print(f"  remove:  {len(plan_remove)}")
    print(f"  extra (left untouched): {len(extras) - len(plan_remove)}")
    for item in extras:
        verb = "REMOVE" if args.remove_extras else "keep"
        print(f"    {verb}  {item['videoId']}  {item['title']}  (pos {item['position']})")

    if args.dry_run:
        for pos, vid, label in plan_add:
            print(f"  ADD    pos={pos}  {vid}  {label}")
        for pos, vid, item in plan_reorder:
            print(f"  MOVE   {vid}  pos {item['position']} -> {pos}")
        return 0

    added = moved = removed = failed = 0
    for item in plan_remove:
        try:
            youtube.playlistItems().delete(id=item["id"]).execute()
            print(f"  REMOVE {item['videoId']}  ({item['title']})")
            removed += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL REMOVE {item['videoId']}: {exc}")
            failed += 1
    for pos, vid, label in plan_add:
        try:
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "position": pos,
                        "resourceId": {"kind": "youtube#video", "videoId": vid},
                    }
                },
            ).execute()
            print(f"  ADD  pos={pos}  {vid}  {label}")
            added += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL ADD {vid}: {exc}")
            failed += 1

    for pos, vid, item in plan_reorder:
        try:
            youtube.playlistItems().update(
                part="snippet",
                body={
                    "id": item["id"],
                    "snippet": {
                        "playlistId": playlist_id,
                        "position": pos,
                        "resourceId": {"kind": "youtube#video", "videoId": vid},
                    },
                },
            ).execute()
            print(f"  MOVE {vid}  -> {pos}")
            moved += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL MOVE {vid}: {exc}")
            failed += 1

    print(f"\nAdded {added}, reordered {moved}, removed {removed}, failed {failed}")
    return 1 if failed else 0


def _collect_video_ids_for_publish(sessions_path, lt_yaml_path):
    """Return [(video_id, label), ...] for every video tracked by this conference."""
    pairs = []
    with open(sessions_path, encoding="utf-8") as fp:
        sessions = yaml.safe_load(fp) or []
    for s in sessions:
        if s.get("youtubeId"):
            pairs.append((s["youtubeId"], s.get("title", s["youtubeId"])))
    if lt_yaml_path.exists():
        with open(lt_yaml_path, encoding="utf-8") as fp:
            lt_data = yaml.safe_load(fp) or {}
        for day in lt_data.get("days", []):
            if day.get("youtubeId"):
                pairs.append((day["youtubeId"], day.get("name", day["youtubeId"])))
    return pairs


def cmd_publish(args):
    pairs = _collect_video_ids_for_publish(args.sessions, args.lt_yaml)
    if not pairs:
        print("No videos found to publish.", file=sys.stderr)
        return 1

    print(f"Will set privacyStatus={args.privacy} on {len(pairs)} video(s) + playlist {args.title!r}")
    for vid, label in pairs:
        print(f"  - {vid}  {label}")

    if args.dry_run:
        print("\nDry run: nothing changed.")
        return 0

    youtube = get_youtube_client(args.client_secrets, args.token_file)

    # Fetch existing status so we preserve madeForKids / selfDeclaredMadeForKids.
    statuses = {}
    ids = [v for v, _ in pairs]
    for i in range(0, len(ids), 50):
        batch = ids[i : i + 50]
        resp = youtube.videos().list(part="status", id=",".join(batch)).execute()
        for item in resp.get("items", []):
            statuses[item["id"]] = item["status"]

    updated = skipped = failed = 0
    for vid, label in pairs:
        status = statuses.get(vid)
        if status is None:
            print(f"  SKIP {vid}: not found")
            skipped += 1
            continue
        if status.get("privacyStatus") == args.privacy:
            print(f"  SKIP {vid}: already {args.privacy}")
            skipped += 1
            continue
        new_status = dict(status)
        new_status["privacyStatus"] = args.privacy
        try:
            youtube.videos().update(part="status", body={"id": vid, "status": new_status}).execute()
            print(f"  OK   {vid}: -> {args.privacy}  ({label})")
            updated += 1
        except Exception as exc:  # noqa: BLE001
            print(f"  FAIL {vid}: {exc}")
            failed += 1

    # Playlist privacy.
    playlist = find_playlist_by_title(youtube, args.title)
    if playlist is None:
        print(f"\nPlaylist {args.title!r} not found; skipping playlist privacy update.")
    elif playlist["status"]["privacyStatus"] == args.privacy:
        print(f"\nPlaylist already {args.privacy}.")
    else:
        body = {
            "id": playlist["id"],
            "snippet": {
                "title": playlist["snippet"]["title"],
                "description": playlist["snippet"].get("description", ""),
            },
            "status": {"privacyStatus": args.privacy},
        }
        try:
            youtube.playlists().update(part="snippet,status", body=body).execute()
            print(f"\nPlaylist {playlist['id']} -> {args.privacy}")
        except Exception as exc:  # noqa: BLE001
            print(f"\nFAIL playlist privacy: {exc}")
            failed += 1

    print(f"\nUpdated {updated}, skipped {skipped}, failed {failed}")
    return 1 if failed else 0


def cmd_sync(args):
    sessions = load_sessions(args.sessions)
    candidates = []
    for session in sessions:
        yt_id = session.get("youtubeId")
        if not yt_id:
            continue
        if args.only and yt_id not in args.only:
            continue
        candidates.append((yt_id, session))

    if not candidates:
        print(f"No sessions with youtubeId found in {args.sessions}", file=sys.stderr)
        return 0

    print(f"Found {len(candidates)} session(s) with youtubeId to sync")

    if args.dry_run:
        for yt_id, session in candidates:
            title = build_title(session)
            description = build_description(session, args.conf_url)
            print(f"\n--- https://www.youtube.com/watch?v={yt_id} ---")
            print(f"Title ({len(title)} chars): {title}")
            print(f"Description ({len(description)} chars):")
            print(description)
        return 0

    youtube = get_youtube_client(args.client_secrets, args.token_file)
    existing = fetch_existing(youtube, [yid for yid, _ in candidates])

    updated = skipped = failed = 0
    for yt_id, session in candidates:
        snippet = existing.get(yt_id)
        if snippet is None:
            print(f"  SKIP {yt_id}: not found on YouTube (or not owned by authorized account)")
            skipped += 1
            continue

        title = build_title(session)
        description = build_description(session, args.conf_url)

        if snippet.get("title") == title and snippet.get("description") == description:
            print(f"  SKIP {yt_id}: already in sync")
            skipped += 1
            continue

        try:
            update_video(youtube, yt_id, snippet, title, description)
            print(f"  OK   {yt_id}: {title}")
            updated += 1
        except Exception as exc:  # noqa: BLE001 - surfaced to operator
            print(f"  FAIL {yt_id}: {exc}")
            failed += 1

    print(f"\nUpdated {updated}, skipped {skipped}, failed {failed}")
    return 1 if failed else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument("--sessions", type=Path, default=DEFAULT_SESSIONS,
                        help=f"Sessions YAML (default: {DEFAULT_SESSIONS.relative_to(REPO_ROOT)})")
    parser.add_argument("--client-secrets", type=Path, default=DEFAULT_CLIENT_SECRETS,
                        help="OAuth client secrets JSON")
    parser.add_argument("--token-file", type=Path, default=DEFAULT_TOKEN_FILE,
                        help="Cached OAuth token JSON")

    sub = parser.add_subparsers(dest="command", required=True)

    p_match = sub.add_parser("match", help="Fuzzy-match channel uploads to sessions; write youtubeId to YAML")
    p_match.add_argument("--threshold", type=float, default=0.55,
                         help="Minimum similarity ratio to accept a match (0.0–1.0, default 0.55)")
    p_match.add_argument("--channel", default=None,
                         help="Channel handle, URL, or ID to read uploads from (e.g. @writethedocs). Defaults to authenticated account.")
    p_match.add_argument("--dry-run", action="store_true", help="Preview without writing")
    p_match.set_defaults(func=cmd_match)

    p_sync = sub.add_parser("sync", help="Push titles + descriptions to YouTube for sessions with youtubeId")
    p_sync.add_argument("--conf-url", default=DEFAULT_CONF_URL,
                        help="Conference URL included in each description")
    p_sync.add_argument("--only", action="append", default=[],
                        help="Only sync these YouTube IDs (repeatable)")
    p_sync.add_argument("--dry-run", action="store_true", help="Preview without writing")
    p_sync.set_defaults(func=cmd_sync)

    p_lt = sub.add_parser("lt", help="Sync lightning-talk video titles/descriptions from the LT YAML")
    p_lt.add_argument("--lt-yaml", type=Path, default=DEFAULT_LT_YAML,
                      help=f"Lightning-talks YAML (default: {DEFAULT_LT_YAML.relative_to(REPO_ROOT)})")
    p_lt.add_argument("--dry-run", action="store_true", help="Preview without writing")
    p_lt.set_defaults(func=cmd_lt)

    p_playlist = sub.add_parser("playlist", help="Find/create the conference playlist and add videos in schedule order")
    p_playlist.add_argument("--schedule", type=Path, default=DEFAULT_SCHEDULE,
                            help=f"Schedule YAML (default: {DEFAULT_SCHEDULE.relative_to(REPO_ROOT)})")
    p_playlist.add_argument("--lt-yaml", type=Path, default=DEFAULT_LT_YAML,
                            help="Lightning-talks YAML")
    p_playlist.add_argument("--title", default=DEFAULT_PLAYLIST_TITLE,
                            help="Playlist title to find or create")
    p_playlist.add_argument("--description", default=DEFAULT_PLAYLIST_DESCRIPTION,
                            help="Description applied when creating a new playlist")
    p_playlist.add_argument("--privacy", choices=["public", "unlisted", "private"], default="public",
                            help="Privacy level applied when creating a new playlist")
    p_playlist.add_argument("--reorder", action="store_true",
                            help="Also reorder existing items to match the desired sequence")
    p_playlist.add_argument("--remove-extras", action="store_true",
                            help="Remove playlist items whose video isn't in the desired set")
    p_playlist.add_argument("--no-auth", action="store_true",
                            help="(Dry-run only) Skip YouTube auth and just print the desired order")
    p_playlist.add_argument("--create-only-if-dry-run", action="store_true", help=argparse.SUPPRESS)
    p_playlist.add_argument("--dry-run", action="store_true", help="Preview without writing")
    p_playlist.set_defaults(func=cmd_playlist)

    p_publish = sub.add_parser("publish", help="Set privacy on all tracked videos + the conference playlist")
    p_publish.add_argument("--lt-yaml", type=Path, default=DEFAULT_LT_YAML,
                           help="Lightning-talks YAML (optional)")
    p_publish.add_argument("--title", default=DEFAULT_PLAYLIST_TITLE,
                           help="Playlist title to update")
    p_publish.add_argument("--privacy", choices=["public", "unlisted", "private"], default="public",
                           help="Privacy level to set (default: public)")
    p_publish.add_argument("--dry-run", action="store_true", help="Preview without writing")
    p_publish.set_defaults(func=cmd_publish)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
