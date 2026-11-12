#!/usr/bin/env python3
"""Check that images referenced in page front matter exist.

Pages reference their social-preview image and hero banner via front matter
(``og:image:`` / ``banner:`` in Markdown, ``:og:image:`` / ``:banner:`` in
RST). htmlproofer never sees these: og:image is a <meta> tag and the banner
becomes a CSS background-image, so broken references ship silently.

Jinja variables (``{{shortcode}}``, ``{{year}}``) are resolved from the
page's ``conf/<city>/<year>/`` path and the conference config YAML, the same
way the site renders them.

Usage:
    python lint_frontmatter_images.py docs
"""

import re
import sys
from pathlib import Path

FIELD_RE = re.compile(r"^[ \t]*:?(og:image|banner):[ \t]*(\S+)[ \t]*$", re.M)
SHORTCODE_RE = re.compile(r"^shortcode:\s*(\S+)", re.M)
SKIP_DIRS = {"_build", "include", "node_modules"}


def shortcode_for(docs_dir: Path, city: str, year: str) -> str:
    config = docs_dir / "_data" / f"{city}-{year}-config.yaml"
    if config.exists():
        match = SHORTCODE_RE.search(config.read_text(encoding="utf-8"))
        if match:
            return match.group(1)
    return city


def check_file(docs_dir: Path, path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    errors = []
    for match in FIELD_RE.finditer(text):
        line_no = text[: match.start()].count("\n")
        if lines[line_no].lstrip().startswith("#"):
            continue  # commented out
        field, value = match.groups()
        if "://" in value:
            continue  # external URL
        if "{{" in value:
            parts = path.relative_to(docs_dir).parts
            if len(parts) >= 3 and parts[0] == "conf":
                city, year = parts[1], parts[2]
                value = value.replace("{{shortcode}}", shortcode_for(docs_dir, city, year))
                value = value.replace("{{ shortcode }}", shortcode_for(docs_dir, city, year))
                value = value.replace("{{year}}", year).replace("{{ year }}", year)
        if "{{" in value:
            errors.append(f"  line {line_no + 1}: cannot resolve {field}: {match.group(2)}")
        elif not (docs_dir / value.lstrip("/")).exists():
            errors.append(f"  line {line_no + 1}: {field} file not found: {value}")
    return errors


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <docs-dir>")
        sys.exit(2)

    docs_dir = Path(sys.argv[1])
    if not docs_dir.is_dir():
        print(f"ERROR: {docs_dir} is not a directory")
        sys.exit(2)

    failed = False
    for page in sorted(docs_dir.rglob("*")):
        if page.suffix not in (".rst", ".md"):
            continue
        if SKIP_DIRS & set(page.relative_to(docs_dir).parts):
            continue
        errors = check_file(docs_dir, page)
        if errors:
            failed = True
            print(f"{page.relative_to(docs_dir)}:")
            for err in errors:
                print(err)

    if failed:
        print()
        print("ERROR: Found front-matter references to images that do not exist.")
        print("These render as broken social previews or hero banners.")
        sys.exit(1)
    else:
        print("OK: All front-matter image references resolve.")


if __name__ == "__main__":
    main()
