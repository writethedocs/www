#!/usr/bin/env python3
"""Check built HTML for markup that was not parsed by Sphinx/MyST.

Detects literal directive syntax in rendered HTML output (outside of code
blocks, scripts, styles, and comments) which indicates that a directive was
silently swallowed — e.g. by a CommonMark HTML block absorbing a MyST fence.

Usage:
    python check_unparsed_markup.py docs/_build/html
"""

import re
import sys
from pathlib import Path

# MyST directive fences: ```{name} or ```{name-with-hyphens}
MYST_DIRECTIVE_RE = re.compile(r"```\{[a-z][-a-z_]*\}")

# RST directives: .. name:: or .. name-with-hyphens::
RST_DIRECTIVE_RE = re.compile(r"\.\.\s+[a-z][-a-z_]*::")

# Blocks to strip before checking — code examples, scripts, styles, and
# comments may legitimately contain directive-like syntax.
STRIP_BLOCKS_RE = re.compile(
    r"<(?:pre|code|script|style)[^>]*>.*?</(?:pre|code|script|style)>"
    r"|<!--.*?-->",
    re.DOTALL,
)


def check_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")

    # Fast path: skip expensive stripping if no directive-like text present
    if "```{" not in text and ".. " not in text:
        return []

    cleaned = STRIP_BLOCKS_RE.sub("", text)

    errors = []
    for match in MYST_DIRECTIVE_RE.finditer(cleaned):
        errors.append(f"  Unparsed MyST directive: {match.group()}")
    for match in RST_DIRECTIVE_RE.finditer(cleaned):
        errors.append(f"  Unparsed RST directive: {match.group()}")
    return errors


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <build-dir>")
        sys.exit(2)

    build_dir = Path(sys.argv[1])
    if not build_dir.is_dir():
        print(f"ERROR: {build_dir} is not a directory")
        sys.exit(2)

    failed = False
    for html_file in sorted(build_dir.rglob("*.html")):
        errors = check_file(html_file)
        if errors:
            failed = True
            rel = html_file.relative_to(build_dir)
            print(f"{rel}:")
            for err in errors:
                print(err)

    if failed:
        print()
        print("ERROR: Found unparsed directive markup in build output.")
        print("This usually means raw HTML or bad indentation prevented the parser")
        print("from recognizing a directive. Ensure a blank line before directive fences")
        print("and check RST indentation.")
        sys.exit(1)
    else:
        print("OK: No unparsed directive markup found.")


if __name__ == "__main__":
    main()
