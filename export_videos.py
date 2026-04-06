#!/usr/bin/env python3
"""
Export all YouTube video titles, IDs, and slugs from the Write the Docs
YouTube channel, fetched directly via yt-dlp.

Fetches all playlists first, then each playlist's videos, plus any
channel-level uploads not in a playlist.

Requires: pip install yt-dlp
"""

import csv
import re
import subprocess
import sys

CHANNEL_URL = "https://www.youtube.com/c/WritetheDocs"


def slugify(text):
    """Create a URL-appropriate slug from a string."""
    slug = text.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def yt_dlp_list(url):
    """Run yt-dlp --flat-playlist and return list of (id, title) tuples."""
    result = subprocess.run(
        [
            "yt-dlp",
            "--no-check-certificates",
            "--print", "%(id)s\t%(title)s",
            "--no-abort-on-error",
            "--flat-playlist",
            url,
        ],
        capture_output=True,
        text=True,
        timeout=120,
    )
    items = []
    for line in result.stdout.strip().splitlines():
        parts = line.split("\t", 1)
        if len(parts) == 2:
            items.append((parts[0], parts[1]))
    return items


def main():
    # 1. Fetch all playlists
    print("Fetching playlists...")
    playlists = yt_dlp_list(f"{CHANNEL_URL}/playlists")
    print(f"Found {len(playlists)} playlists")

    # 2. Fetch videos from each playlist
    all_videos = []
    seen_ids = set()

    for pl_id, pl_title in playlists:
        url = f"https://www.youtube.com/playlist?list={pl_id}"
        print(f"  {pl_title} ...", end=" ", flush=True)
        items = yt_dlp_list(url)
        count = 0
        for vid, title in items:
            if vid not in seen_ids:
                seen_ids.add(vid)
                all_videos.append({
                    "title": title,
                    "youtubeId": vid,
                    "slug": slugify(title),
                    "playlist": pl_title,
                    "playlistId": pl_id,
                })
                count += 1
        print(f"{len(items)} videos ({count} new)")

    # 3. Fetch channel uploads to catch videos not in any playlist
    print("  Channel uploads ...", end=" ", flush=True)
    channel_videos = yt_dlp_list(f"{CHANNEL_URL}/videos")
    count = 0
    for vid, title in channel_videos:
        if vid not in seen_ids:
            seen_ids.add(vid)
            all_videos.append({
                "title": title,
                "youtubeId": vid,
                "slug": slugify(title),
                "playlist": "",
                "playlistId": "",
            })
            count += 1
    print(f"{count} additional videos")

    # 4. Write CSV
    output_path = "youtube_videos.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["title", "youtubeId", "slug", "playlist", "playlistId"]
        )
        writer.writeheader()
        writer.writerows(all_videos)

    print(f"\nExported {len(all_videos)} unique videos to {output_path}")


if __name__ == "__main__":
    main()
