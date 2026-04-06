#!/usr/bin/env python3
"""
Export all YouTube video titles, IDs, and slugs from the Write the Docs
YouTube channel, fetched directly via yt-dlp.
"""

import csv
import re
import subprocess
import sys


def slugify(text):
    """Create a URL-appropriate slug from a string."""
    slug = text.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def main():
    channel_url = "https://www.youtube.com/c/WritetheDocs/videos"

    print(f"Fetching videos from {channel_url} ...")
    result = subprocess.run(
        [
            "yt-dlp",
            "--no-check-certificates",
            "--print", "%(id)s\t%(title)s",
            "--no-abort-on-error",
            "--flat-playlist",
            channel_url,
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0 and not result.stdout.strip():
        print("yt-dlp failed:", result.stderr, file=sys.stderr)
        sys.exit(1)

    videos = []
    for line in result.stdout.strip().splitlines():
        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        video_id, title = parts
        videos.append({
            "title": title,
            "youtubeId": video_id,
            "slug": slugify(title),
        })

    output_path = "youtube_videos.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "youtubeId", "slug"])
        writer.writeheader()
        writer.writerows(videos)

    print(f"Exported {len(videos)} videos to {output_path}")


if __name__ == "__main__":
    main()
