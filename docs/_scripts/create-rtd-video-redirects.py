#!/usr/bin/env python3
"""
Create Read the Docs redirects for old /videos/ URLs to YouTube.

Reads speaker/session YAML data to build a mapping of video slugs to
YouTube video IDs, then creates exact redirects via the RTD API so that
old /videos/<region>/<year>/<slug>/ URLs redirect to the correct YouTube
video page.

Requires:
    - RTD_TOKEN environment variable (Read the Docs API token)
    - PyYAML and requests packages

Usage:
    RTD_TOKEN=<token> python docs/_scripts/create-rtd-video-redirects.py
    RTD_TOKEN=<token> python docs/_scripts/create-rtd-video-redirects.py --dry-run
"""

import argparse
import glob
import io
import os
import re
import sys
import time

import requests
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(REPO_ROOT, "docs", "_data")

RTD_PROJECT = "writethedocs-www"
RTD_API_URL = f"https://readthedocs.org/api/v3/projects/{RTD_PROJECT}/redirects/"
CHANNEL_URL = "https://www.youtube.com/c/WritetheDocs"

SPEAKERS_PATTERN = re.compile(r"(\d{4})\.(\w+)\.speakers")
SESSIONS_PATTERN = re.compile(r"(\w+)-(\d{4})-sessions")

KNOWN_PLAYLISTS = {
    ("eu", 2014): "PLZAeFn6dfHpnHBLE4qEUwg1LjhDZEvC2A",
    ("eu", 2015): "PLZAeFn6dfHplFNTsVdBuHk6vPZbsvHtDw",
    ("eu", 2016): "PLZAeFn6dfHpnN8fXXHwPtPY33aLGGhYLJ",
    ("eu", 2017): "PLZAeFn6dfHplBYPCwJt6ItkMDt7JSgUiL",
    ("na", 2017): "PLZAeFn6dfHpkBld-70TsOoYToM3CaTxRC",
    ("portland", 2017): "PLZAeFn6dfHpkBld-70TsOoYToM3CaTxRC",
    ("portland", 2018): "PLZAeFn6dfHplUgfLOLEuHHAm1HdrIyaZ7",
    ("portland", 2019): "PLZAeFn6dfHpmuHCu5qsIkmp9H5jFD-xq-",
    ("portland", 2020): "PLZAeFn6dfHpkBJAPYFrob6gqdiBuePwGJ",
    ("portland", 2021): "PLZAeFn6dfHpkCk5Fw5yLFGTqd1OJoaXhR",
    ("portland", 2022): "PLZAeFn6dfHpnDhFvXG8GprqlLlzSQRBui",
    ("portland", 2023): "PLZAeFn6dfHpneQPsDWa4OmEpgW4pNiaZ2",
    ("portland", 2024): "PLZAeFn6dfHpm4FboYSTD1Bs8Yp8k_JvAL",
    ("portland", 2025): "PLZAeFn6dfHplMbtJtidqFFtL7rt3ASNSR",
    ("prague", 2017): "PLZAeFn6dfHplBYPCwJt6ItkMDt7JSgUiL",
    ("prague", 2018): "PLZAeFn6dfHplRZcYDQjST22bAVeeWML4d",
    ("prague", 2019): "PLZAeFn6dfHpkpYchP1iFnQnc7i-2xJd0I",
    ("prague", 2020): "PLZAeFn6dfHpmRWZJaUwQzsdagW2TtRI2x",
    ("prague", 2021): "PLZAeFn6dfHpnaoiOQyd9BYbQbprDGQjQ9",
    ("prague", 2022): "PLZAeFn6dfHpm1PRgp84X5jh9Jca_KTJSF",
    ("australia", 2018): "PLy70RNJ7dYrJB-2yuGw-bTppEDmQr5T56",
    ("australia", 2020): "PLZAeFn6dfHpl2E5JhVd34llZD4a4oAeCo",
    ("australia", 2022): "PLZAeFn6dfHpktOcWn5mQNOx5gYo6O7TR6",
    ("au", 2017): "PLy70RNJ7dYrJR66QtoHmTWSqm4iAlmH-m",
}


def slugify(text):
    slug = text.encode("utf-8", "ignore").lower().decode("utf-8")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    slug = re.sub(r"[-]+", "-", slug)
    return slug


def generate_video_slug(session):
    if "slug" in session:
        return session["slug"]
    if "title" not in session:
        return ""
    title = session["title"]
    for speaker in session.get("speakers", []):
        title += "-{}".format(speaker.get("slug", speaker["name"]))
    return slugify(title)


def extract_youtube_id(session):
    if session.get("youtubeId"):
        return session["youtubeId"]
    path = session.get("path", "")
    if path and "youtube.com" in path:
        mo = re.search(r"watch\?v=([\w-]+)", path)
        if mo:
            return mo.group(1)
    return None


def collect_redirects():
    redirects = []
    listing_pages = set()

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
            sessions = yaml.safe_load(fp) or []

        has_any_video = False
        for session in sessions:
            slug = generate_video_slug(session)
            if not slug:
                continue
            youtube_id = extract_youtube_id(session)
            if not youtube_id:
                continue

            has_any_video = True
            from_url = f"/en/latest/videos/{region}/{year}/{slug}/"
            to_url = f"https://www.youtube.com/watch?v={youtube_id}"
            redirects.append((from_url, to_url))

        if has_any_video:
            listing_pages.add((region, year))

    # Year listing pages -> playlists
    for region, year in sorted(listing_pages):
        playlist_id = KNOWN_PLAYLISTS.get((region, year))
        target = (
            f"https://www.youtube.com/playlist?list={playlist_id}"
            if playlist_id
            else CHANNEL_URL
        )
        from_url = f"/en/latest/videos/{region}/{year}/"
        redirects.append((from_url, target))

    # Main /videos/ index
    redirects.append(("/en/latest/videos/", CHANNEL_URL))

    return redirects


def create_redirect(token, from_url, to_url, dry_run=False):
    if dry_run:
        print(f"  {from_url} -> {to_url}")
        return True

    resp = requests.post(
        RTD_API_URL,
        headers={"Authorization": f"Token {token}"},
        json={
            "redirect_type": "exact",
            "from_url": from_url,
            "to_url": to_url,
        },
    )

    if resp.status_code == 201:
        return True
    elif resp.status_code == 429:
        # Rate limited — wait and retry
        retry_after = int(resp.headers.get("Retry-After", 60))
        print(f"  Rate limited, waiting {retry_after}s...")
        time.sleep(retry_after)
        return create_redirect(token, from_url, to_url, dry_run)
    else:
        print(f"  FAILED ({resp.status_code}): {from_url} -> {resp.text[:200]}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Create Read the Docs redirects for video URLs"
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview only")
    args = parser.parse_args()

    token = os.environ.get("RTD_TOKEN")
    if not token and not args.dry_run:
        print("Error: RTD_TOKEN environment variable is required", file=sys.stderr)
        return 1

    redirects = collect_redirects()
    print(f"Found {len(redirects)} redirects to create")

    if args.dry_run:
        for from_url, to_url in sorted(redirects):
            print(f"  {from_url} -> {to_url}")
        print(f"\nDry run: {len(redirects)} redirects would be created")
        return 0

    created = 0
    failed = 0
    for from_url, to_url in sorted(redirects):
        if create_redirect(token, from_url, to_url, dry_run=args.dry_run):
            created += 1
        else:
            failed += 1
        # Be gentle with the API
        time.sleep(0.5)

    print(f"\nCreated {created} redirects, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
