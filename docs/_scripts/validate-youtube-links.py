#!/usr/bin/env python3
"""
Validate YouTube video links in session/speaker YAML files against the
actual Write the Docs YouTube channels.

This script:
1. Loads the cached video list from youtube_videos.csv (run export_videos.py
   first to fetch from YouTube, or pass --fetch to do it live)
2. Scans all session/speaker YAML files for YouTube references
3. Reports mismatches: broken IDs, missing videos, unlinked uploads

Usage:
    python docs/_scripts/validate-youtube-links.py
    python docs/_scripts/validate-youtube-links.py --fetch    # fetch fresh data first
    python docs/_scripts/validate-youtube-links.py --verbose  # show all matched videos

Requires: pip install pyyaml (and yt-dlp if using --fetch)
"""

import argparse
import csv
import glob
import io
import os
import re
import subprocess
import sys

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(REPO_ROOT, "docs", "_data")
CSV_PATH = os.path.join(REPO_ROOT, "youtube_videos.csv")
EXPORT_SCRIPT = os.path.join(REPO_ROOT, "export_videos.py")

SPEAKERS_PATTERN = re.compile(r"(\d{4})\.(\w+)\.speakers")
SESSIONS_PATTERN = re.compile(r"(\w+)-(\d{4})-sessions")
YOUTUBE_URL_PATTERN = re.compile(r"https?://(?:www\.)?youtube\.com/watch\?v=([\w-]+)")


def load_youtube_csv():
    """Load the cached YouTube video list from CSV."""
    if not os.path.exists(CSV_PATH):
        print(f"Error: {CSV_PATH} not found.", file=sys.stderr)
        print(f"Run 'python export_videos.py' first, or use --fetch.", file=sys.stderr)
        sys.exit(1)
    videos = {}
    with open(CSV_PATH, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            videos[row["youtubeId"]] = row
    return videos


def extract_youtube_id(session):
    """Extract YouTube video ID from a session dict, checking multiple fields."""
    if session.get("youtubeId"):
        return session["youtubeId"]
    video = session.get("video", "")
    if video and "youtube.com" in video:
        mo = YOUTUBE_URL_PATTERN.search(video)
        if mo:
            return mo.group(1)
    path = session.get("path", "")
    if path and "youtube.com" in path:
        mo = YOUTUBE_URL_PATTERN.search(path)
        if mo:
            return mo.group(1)
    return None


def scan_yaml_files():
    """Scan all session/speaker YAML files and return list of references."""
    refs = []
    for f in sorted(glob.glob(os.path.join(DATA_DIR, "*.yaml"))):
        base = os.path.splitext(os.path.basename(f))[0]

        mo = SPEAKERS_PATTERN.match(base)
        if mo:
            year, region = int(mo.group(1)), mo.group(2)
        else:
            mo = SESSIONS_PATTERN.match(base)
            if mo:
                region, year = mo.group(1), int(mo.group(2))
            else:
                continue

        with io.open(f, encoding="utf-8") as fp:
            sessions = yaml.safe_load(fp)
        if not sessions:
            continue

        for session in sessions:
            title = session.get("title", "(untitled)")
            slug = session.get("slug", "")
            youtube_id = extract_youtube_id(session)
            refs.append({
                "file": os.path.basename(f),
                "year": year,
                "region": region,
                "title": title,
                "slug": slug,
                "youtubeId": youtube_id,
            })
    return refs


def validate(youtube_videos, yaml_refs, verbose=False):
    """Compare YAML references against YouTube channel data. Returns error count."""
    broken = []
    matched = []
    yaml_ids_seen = set()
    sessions_without_video = []

    for ref in yaml_refs:
        yt_id = ref["youtubeId"]
        if not yt_id:
            sessions_without_video.append(ref)
            continue

        yaml_ids_seen.add(yt_id)
        if yt_id in youtube_videos:
            matched.append(ref)
        else:
            broken.append(ref)

    youtube_only = {
        vid: info for vid, info in youtube_videos.items()
        if vid not in yaml_ids_seen
    }

    # --- Report ---
    print("\n" + "=" * 70)
    print("YouTube Link Validation Report")
    print("=" * 70)

    total_sessions = len(yaml_refs)
    with_video = len(matched) + len(broken)
    print(f"\nSessions in YAML files:          {total_sessions}")
    print(f"  With YouTube link:             {with_video}")
    print(f"  Without YouTube link:          {len(sessions_without_video)}")
    print(f"Videos on YouTube channels:      {len(youtube_videos)}")

    if broken:
        print(f"\n{'!' * 70}")
        print(f"BROKEN: {len(broken)} YouTube IDs in YAML not found on any channel")
        print(f"{'!' * 70}")
        for ref in sorted(broken, key=lambda r: (r["year"], r["region"])):
            print(f"  [{ref['file']}] {ref['title']}")
            print(f"    ID: {ref['youtubeId']}")
            print(f"    URL: https://www.youtube.com/watch?v={ref['youtubeId']}")
    else:
        print(f"\n  All {len(matched)} YouTube IDs in YAML files are valid!")

    if youtube_only:
        # Group by playlist for readability
        by_playlist = {}
        for vid, info in youtube_only.items():
            pl = info.get("playlist", "") or "(no playlist)"
            by_playlist.setdefault(pl, []).append((vid, info))

        print(f"\n{'-' * 70}")
        print(f"UNLINKED: {len(youtube_only)} videos on YouTube but not in any YAML file")
        print(f"{'-' * 70}")
        for pl in sorted(by_playlist):
            print(f"\n  [{pl}]")
            for vid, info in by_playlist[pl]:
                channel = info.get("channel", "")
                ch_label = f" ({channel})" if channel else ""
                print(f"    {info['title']}{ch_label}")
                print(f"      ID: {vid}")

    if verbose and matched:
        print(f"\n{'-' * 70}")
        print(f"MATCHED: {len(matched)} videos")
        print(f"{'-' * 70}")
        for ref in sorted(matched, key=lambda r: (r["year"], r["region"], r["title"])):
            yt = youtube_videos[ref["youtubeId"]]
            channel = yt.get("channel", "")
            ch_label = f" [{channel}]" if channel else ""
            print(f"  {ref['year']} {ref['region']}: {ref['title']} -> {ref['youtubeId']}{ch_label}")

    # Sessions with no video link, grouped by year/region
    if sessions_without_video:
        by_conf = {}
        for ref in sessions_without_video:
            key = f"{ref['year']} {ref['region']}"
            by_conf.setdefault(key, []).append(ref)

        print(f"\n{'-' * 70}")
        print(f"NO VIDEO: {len(sessions_without_video)} sessions without a YouTube link")
        print(f"{'-' * 70}")
        for key in sorted(by_conf):
            titles = [r["title"] for r in by_conf[key]]
            print(f"  {key}: {len(titles)} sessions")
            if verbose:
                for t in titles:
                    print(f"    - {t}")

    # Summary
    print(f"\n{'=' * 70}")
    print("Summary:")
    print(f"  Matched:    {len(matched):>4}")
    print(f"  Broken:     {len(broken):>4}  {'<-- action needed!' if broken else ''}")
    print(f"  Unlinked:   {len(youtube_only):>4}  (on YouTube, not in YAML)")
    print(f"  No video:   {len(sessions_without_video):>4}  (in YAML, no YouTube link)")
    print(f"{'=' * 70}")

    return len(broken)


def main():
    parser = argparse.ArgumentParser(
        description="Validate YouTube links in Write the Docs session YAML files"
    )
    parser.add_argument(
        "--fetch", action="store_true",
        help="Run export_videos.py to fetch fresh data from YouTube before validating"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show all matched videos and sessions without links"
    )
    args = parser.parse_args()

    if args.fetch:
        print("Fetching fresh data from YouTube...")
        result = subprocess.run(
            [sys.executable, EXPORT_SCRIPT],
            cwd=REPO_ROOT,
        )
        if result.returncode != 0:
            print("Error: export_videos.py failed", file=sys.stderr)
            sys.exit(1)
        print()

    youtube_videos = load_youtube_csv()
    print(f"Loaded {len(youtube_videos)} videos from {CSV_PATH}")

    yaml_refs = scan_yaml_files()
    print(f"Scanned {len(yaml_refs)} sessions from YAML files")

    error_count = validate(youtube_videos, yaml_refs, verbose=args.verbose)
    sys.exit(1 if error_count else 0)


if __name__ == "__main__":
    main()
