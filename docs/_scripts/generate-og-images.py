"""Generate conference opengraph images from the built index pages.

Renders each conference's real index-page hero (nav and CTA buttons hidden)
with headless Chromium and saves it as the conference's opengraph image:

    docs/_static/conf/images/headers/<shortcode>-<year>-opengraph.jpg

The screenshot is taken at half the target size with a 2x device scale
factor, so the hero text is proportionally large enough to stay legible when
social platforms display the image as a ~500px card thumbnail.

Usage (from the repo root, after building the site):

    cd docs && uv run make html && cd ..
    uv run python docs/_scripts/generate-og-images.py berlin/2026 australia/2026

    # Write somewhere else, or check a thumbnail-size QA sheet:
    uv run python docs/_scripts/generate-og-images.py berlin/2026 \\
        --out-dir /tmp/og --preview /tmp/og/preview.jpg

Run it whenever a conference's index page goes live or its hero changes,
then commit the regenerated JPEGs. Chromium is found via --chromium,
$OG_CHROMIUM, $CHROME_BIN, common binary names on $PATH, or an installed
Playwright Chromium. The site's fonts (Bree Serif, Nunito Sans) are
downloaded from Google Fonts on first run and cached in docs/_build/og-fonts,
because headless Chromium does not load webfonts from a file:// page.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml
from PIL import Image

REPO = Path(__file__).resolve().parents[2]

# Output size follows the existing <conf>-opengraph.jpg convention (a wide
# ~3:1 banner). The page is laid out at half this size and rendered at
# device-scale-factor 2, which doubles the text size relative to the frame.
OUT_W, OUT_H = 2006, 660
CSS_W, CSS_H = OUT_W // 2, OUT_H // 2

# The classic (non-css2) endpoint returns one plain @font-face block with a
# TTF URL per family/weight when requested without a browser user agent.
FONTS_CSS_URL = "https://fonts.googleapis.com/css?family=Nunito+Sans:400,700,800|Bree+Serif"

CHROMIUM_CANDIDATES = [
    "chromium",
    "chromium-browser",
    "google-chrome",
    "google-chrome-stable",
    "headless_shell",
]


def find_chromium(explicit):
    for candidate in [explicit, os.environ.get("OG_CHROMIUM"), os.environ.get("CHROME_BIN")]:
        if candidate:
            return candidate
    for name in CHROMIUM_CANDIDATES:
        if path := shutil.which(name):
            return path
    # Playwright-managed browsers (e.g. Claude Code / CI containers)
    pw_root = Path(os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "~/.cache/ms-playwright")).expanduser()
    for pattern in ["chromium_headless_shell-*/chrome-linux/headless_shell",
                    "chromium-*/chrome-linux/chrome"]:
        if found := sorted(pw_root.glob(pattern)):
            return str(found[-1])
    sys.exit("error: no Chromium binary found; pass --chromium or set $OG_CHROMIUM")


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": ""})
    with urllib.request.urlopen(request) as response:
        return response.read()


def ensure_fonts(cache_dir):
    """Download the site's fonts once and return @font-face CSS for them."""
    faces = []
    css_path = cache_dir / "fonts.css"
    if not css_path.exists():
        cache_dir.mkdir(parents=True, exist_ok=True)
        css = fetch(FONTS_CSS_URL).decode("utf-8")
        for block in re.findall(r"@font-face\s*{[^}]*}", css):
            family = re.search(r"font-family:\s*'([^']+)'", block).group(1)
            weight = re.search(r"font-weight:\s*(\d+)", block).group(1)
            url = re.search(r"url\(([^)]+)\)", block).group(1)
            filename = f"{family.lower().replace(' ', '-')}-{weight}.ttf"
            (cache_dir / filename).write_bytes(fetch(url))
            faces.append(
                f"@font-face {{ font-family: '{family}'; font-weight: {weight}; "
                f"src: url('file://{cache_dir / filename}'); }}")
        css_path.write_text("".join(faces), encoding="utf-8")
        print(f"fonts cached in {cache_dir}")
    return css_path.read_text(encoding="utf-8")


def page_css(font_css):
    # Hide navigation, calls to action, and everything below the hero, then
    # size the hero to exactly the capture area with its content centered.
    return (
        f"<style>{font_css}</style>"
        "<style>"
        "  .hero nav, .ctas-block, .announcement, .page-content, section,"
        "  footer, .footer, readthedocs-flyout, readthedocs-notification"
        "  { display: none !important; }"
        "  body { background: #ffffff; }"
        f" .hero {{ min-height: {CSS_H}px !important; display: flex !important;"
        "          align-items: center !important; }"
        "  .hero .hero-content { width: 100%; }"
        "</style>"
    )


def shortcode_for(city, year):
    config = REPO / "docs" / "_data" / f"{city}-{year}-config.yaml"
    if config.exists():
        return yaml.safe_load(config.read_text()).get("shortcode", city)
    return city


def screenshot(chromium, page, out_png):
    """Render the modified page and return the cropped hero as a PIL image."""
    subprocess.run(
        [chromium, "--headless", "--no-sandbox", "--disable-gpu",
         "--hide-scrollbars", "--ignore-certificate-errors",
         "--force-device-scale-factor=2",
         f"--window-size={CSS_W},{CSS_H + 40}", "--virtual-time-budget=15000",
         f"--screenshot={out_png}", f"file://{page}"],
        check=True, capture_output=True)
    return Image.open(out_png).convert("RGB").crop((0, 0, OUT_W, OUT_H))


def generate(chromium, css, build_dir, out_dir, city, year):
    index = build_dir / "conf" / city / year / "index.html"
    if not index.exists():
        sys.exit(f"error: {index} not found — build the site first (cd docs && uv run make html)")
    og_page = index.with_name("index-og.html")
    out_png = index.with_name("index-og.png")
    try:
        og_page.write_text(
            index.read_text(encoding="utf-8").replace("</head>", css + "</head>"),
            encoding="utf-8")
        image = screenshot(chromium, og_page, out_png)
    finally:
        og_page.unlink(missing_ok=True)
        out_png.unlink(missing_ok=True)
    dest = out_dir / f"{shortcode_for(city, year)}-{year}-opengraph.jpg"
    image.save(dest, quality=88, optimize=True)
    print(dest)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("conferences", nargs="+", metavar="city/year",
                        help="conferences to render, e.g. berlin/2026")
    parser.add_argument("--build-dir", type=Path, default=REPO / "docs" / "_build" / "html")
    parser.add_argument("--out-dir", type=Path,
                        default=REPO / "docs" / "_static" / "conf" / "images" / "headers")
    parser.add_argument("--chromium", help="path to a Chromium/Chrome binary")
    parser.add_argument("--preview", type=Path,
                        help="also write a thumbnail-size QA sheet to this path")
    args = parser.parse_args()

    chromium = find_chromium(args.chromium)
    css = page_css(ensure_fonts(args.build_dir.parent / "og-fonts"))
    args.out_dir.mkdir(parents=True, exist_ok=True)
    images = []
    for conference in args.conferences:
        city, _, year = conference.partition("/")
        if not (city and year):
            sys.exit(f"error: expected city/year, got {conference!r}")
        images.append(generate(chromium, css, args.build_dir, args.out_dir, city, year))

    if args.preview:
        # Preview at ~500px wide: the size social platforms actually display.
        thumb_w = 510
        thumb_h = round(thumb_w * OUT_H / OUT_W)
        sheet = Image.new("RGB", (thumb_w, (thumb_h + 10) * len(images) + 10), "white")
        for i, image in enumerate(images):
            thumb = image.copy()
            thumb.thumbnail((thumb_w, thumb_h))
            sheet.paste(thumb, (0, 10 + i * (thumb_h + 10)))
        sheet.save(args.preview, quality=88)
        print(args.preview)


if __name__ == "__main__":
    main()
