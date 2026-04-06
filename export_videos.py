#!/usr/bin/env python3
"""
Export all YouTube video titles, IDs, and slugs from the Write the Docs
YouTube channels, fetched directly via yt-dlp.

Covers both channels:
  - Main: https://www.youtube.com/c/WritetheDocs
  - Australia: https://www.youtube.com/c/WriteTheDocsAus

Requires: pip install yt-dlp
"""

import csv
import re
import subprocess
import sys

CHANNELS = [
    ("https://www.youtube.com/c/WritetheDocs", "Write the Docs"),
    ("https://www.youtube.com/c/WriteTheDocsAus", "Write the Docs Australia"),
]


def slugify(text):
    slug = text.encode("utf-8", "ignore").lower().decode("utf-8")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    slug = re.sub(r"[-]+", "-", slug)
    return slug


def yt_dlp_list(url):
    result = subprocess.run(
        [
            "yt-dlp", "--no-check-certificates",
            "--print", "%(id)s\t%(title)s",
            "--no-abort-on-error", "--flat-playlist", url,
        ],
        capture_output=True, text=True, timeout=120,
    )
    items = []
    for line in result.stdout.strip().splitlines():
        parts = line.split("\t", 1)
        if len(parts) == 2:
            items.append((parts[0], parts[1]))
    return items


def main():
    all_videos = []
    seen_ids = set()

    for channel_url, channel_name in CHANNELS:
        print(f"\n{'='*60}")
        print(f"Channel: {channel_name}")
        print(f"{'='*60}")

        # Fetch playlists
        print("Fetching playlists...")
        playlists = yt_dlp_list(f"{channel_url}/playlists")
        print(f"  Found {len(playlists)} playlists")

        # Fetch videos from each playlist
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
                        "channel": channel_name,
                    })
                    count += 1
            print(f"{len(items)} videos ({count} new)")

        # Fetch channel uploads
        print("  Channel uploads ...", end=" ", flush=True)
        channel_videos = yt_dlp_list(f"{channel_url}/videos")
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
                    "channel": channel_name,
                })
                count += 1
        print(f"{count} additional videos")

    # Write CSV
    output_path = "youtube_videos.csv"
    fieldnames = ["title", "youtubeId", "slug", "playlist", "playlistId", "channel"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_videos)

    print(f"\nExported {len(all_videos)} unique videos to {output_path}")


if __name__ == "__main__":
    main()
