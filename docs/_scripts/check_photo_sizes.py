#!/usr/bin/env python3
"""Check that photos stay small enough for fast pages.

Banner and page photos live once in docs/_static/conf/images/photos/ and load
on many pages, so a full-size camera file there slows the whole site. This
fails when a photo is over MAX_KB. Banners are cropped to 1600x533 and photos
in text to 800x533, which at JPEG quality 70 comes to about 40-150 KB.

Usage:
    python check_photo_sizes.py [docs/_static/conf/images/photos | photo.jpg ...]
"""

import sys
from pathlib import Path

MAX_KB = 200
PHOTOS = Path("docs/_static/conf/images/photos")


def main(args: list[str]) -> int:
    paths = [Path(a) for a in args] or sorted(PHOTOS.iterdir())
    too_big = [(p, p.stat().st_size // 1024) for p in paths if p.stat().st_size > MAX_KB * 1024]
    for path, kb in too_big:
        print(f"{path}: {kb} KB, over the {MAX_KB} KB limit")
    if too_big:
        print("\nCrop banners to 1600x533 and photos in text to 800x533, "
              "and save them at JPEG quality 70.")
        return 1
    print(f"Checked {len(paths)} photos: all under {MAX_KB} KB.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
