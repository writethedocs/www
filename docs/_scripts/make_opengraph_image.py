#!/usr/bin/env python3
"""Draw a conference's link preview image from its config.

The image is what X, Slack, LinkedIn and the like show when someone shares a
link to the conference: the Write the Docs name, the event and year, the
tagline, and the place and dates, over a photo tinted in the event's colour.
It is drawn at 1200x630, the Open Graph size, so nothing gets cropped.

The pages find it by name, so the output goes to
docs/_static/conf/images/headers/<shortcode>-<year>-opengraph.jpg and nothing
else needs changing. The fonts are the site's, Bree Serif and Nunito Sans,
fetched from Google Fonts into a cache the first time.

Usage:
    python docs/_scripts/make_opengraph_image.py <city>-<year> <photo> [--tagline TEXT]

    python docs/_scripts/make_opengraph_image.py portland-2026 \\
        docs/_static/conf/images/photos/group-2026-55264515839.jpg
"""

import argparse
import sys
import urllib.request
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

DOCS = Path(__file__).resolve().parent.parent
HEADERS = DOCS / "_static/conf/images/headers"
FONT_CACHE = Path.home() / ".cache/writethedocs-fonts"
FONTS = {
    "serif": "ofl/breeserif/BreeSerif-Regular.ttf",
    "sans": "ofl/nunitosans/NunitoSans[YTLC,opsz,wdth,wght].ttf",
}
FONT_URL = "https://raw.githubusercontent.com/google/fonts/main/"

WIDTH, HEIGHT = 1200, 630
SCALE = 2  # Drawn at twice the size so text stays crisp on high-density screens.
TAGLINE = "A conference about software\ndocumentation and community"
DARK = (26, 26, 26)
WHITE = (255, 255, 255)


def font_path(name: str) -> Path:
    """Return the font file, downloading it from Google Fonts on first use."""
    path = FONT_CACHE / Path(FONTS[name]).name
    if not path.exists():
        FONT_CACHE.mkdir(parents=True, exist_ok=True)
        url = FONT_URL + urllib.request.quote(FONTS[name])
        print(f"Fetching {path.name} from Google Fonts")
        urllib.request.urlretrieve(url, path)
    return path


def font(name: str, size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(font_path(name)), size * SCALE)
    if bold:
        f.set_variation_by_name("Bold")
    return f


def mix(colour: tuple[int, int, int], towards: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    return tuple(round(c + (t - c) * amount) for c, t in zip(colour, towards))


def background(colour: tuple[int, int, int], photo: Path) -> Image.Image:
    """The photo, desaturated, under a gradient of the event colour."""
    w, h = WIDTH * SCALE, HEIGHT * SCALE
    top, bottom = mix(colour, WHITE, 0.05), mix(colour, WHITE, 0.45)
    gradient = Image.new("RGB", (1, h))
    for y in range(h):
        gradient.putpixel((0, y), mix(top, bottom, y / (h - 1)))
    gradient = gradient.resize((w, h))

    im = Image.open(photo).convert("RGB")
    pw, ph = im.size
    if pw / ph > WIDTH / HEIGHT:  # wider than the card: crop the sides
        cw = round(ph * WIDTH / HEIGHT)
        im = im.crop(((pw - cw) // 2, 0, (pw - cw) // 2 + cw, ph))
    else:  # taller: crop the top and bottom
        ch = round(pw * HEIGHT / WIDTH)
        im = im.crop((0, (ph - ch) // 2, pw, (ph - ch) // 2 + ch))
    im = ImageEnhance.Color(im.resize((w, h), Image.LANCZOS)).enhance(0.25)
    return Image.blend(gradient, im, 0.22)


def draw(config: dict, photo: Path, tagline: str) -> Image.Image:
    colour = tuple(int(v) for v in str(config["rgb"]).split(","))
    im = background(colour, photo)
    d = ImageDraw.Draw(im)
    s = SCALE

    # Left column: the name stacked, right-aligned against a gutter.
    gutter = 300 * s
    serif = font("serif", 78)
    y = 118 * s
    for word in ("WRITE", "THE", "DOCS"):
        d.text((gutter, y), word, font=serif, fill=DARK, anchor="ra")
        y += 82 * s
    serif_small = font("serif", 44)
    y += 8 * s
    for word in (config["name"].upper(), str(config["year"])):
        d.text((gutter, y), word, font=serif_small, fill=WHITE, anchor="ra")
        y += 48 * s

    # Right column: the tagline, then where and when.
    x = gutter + 46 * s
    d.multiline_text((x, 150 * s), tagline, font=font("sans", 44, bold=True), fill=DARK, spacing=6 * s)
    sans = font("sans", 29, bold=True)
    d.text((x, 300 * s), f"{config['city']}, {config['local_area']}", font=sans, fill=WHITE)
    d.text((x, 342 * s), config["date"]["short"], font=sans, fill=WHITE)
    return im


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("event", help="the config to read, like portland-2026")
    parser.add_argument("photo", type=Path, help="the photo to put behind the text")
    parser.add_argument("--tagline", default=TAGLINE, help="text to the right of the name")
    parser.add_argument("--out", type=Path, help="where to write the image (default: the headers folder)")
    args = parser.parse_args(argv)

    config = yaml.safe_load((DOCS / "_data" / f"{args.event}-config.yaml").read_text())
    out = args.out or HEADERS / f"{config['shortcode']}-{config['year']}-opengraph.jpg"
    im = draw(config, args.photo, args.tagline)
    im.save(out, quality=85, optimize=True, progressive=True)
    print(f"{out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
