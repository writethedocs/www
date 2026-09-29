from docutils import nodes
from docutils.parsers import rst

# Brand color of each conference year, matching $main-color in
# docs/_static/conf/scss/main-<year>.scss.
YEAR_COLORS = {
    2018: "#3dd94a",
    2019: "#ea7852",
    2020: "#3498db",
    2021: "#fdb913",
    2022: "#2ecc71",
    2023: "#ea7852",
    2024: "#4ac1e0",
    2025: "#2ecc71",
    2026: "#fdb913",
    2027: "#ea6852",
}


def conference_year(argument):
    """Validate a ``:year:`` option value against the known brand colors."""
    try:
        year = int(str(argument).strip())
    except ValueError:
        raise ValueError(f"expected a conference year, got {argument!r}")
    if year not in YEAR_COLORS:
        raise ValueError(
            f"no brand color for {year}; add it to YEAR_COLORS in _ext/button.py"
        )
    return year


def contrasting_text_color(background):
    """Return black or white, whichever reads better on ``background``.

    This follows the WCAG contrast formula: work out how bright the
    background is on a 0 (black) to 1 (white) scale, then pick the text
    color with the bigger brightness gap.
    """
    # "#fdb913" -> red=0xfd, green=0xb9, blue=0x13, each scaled to 0..1.
    hex_digits = background.lstrip("#")
    red, green, blue = (int(hex_digits[i : i + 2], 16) / 255 for i in (0, 2, 4))

    def linear(channel):
        # Hex colors are gamma-encoded (sRGB): the number is not proportional
        # to the amount of light, so undo that before mixing the channels.
        if channel <= 0.03928:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4

    # Relative luminance. The weights reflect how sensitive the eye is to
    # each channel: green looks much brighter than the same amount of blue.
    luminance = 0.2126 * linear(red) + 0.7152 * linear(green) + 0.0722 * linear(blue)

    # WCAG contrast is (lighter + 0.05) / (darker + 0.05). Black text wins
    # once the background is brighter than about 0.179, which is where the
    # contrast against black overtakes the contrast against white.
    return "#000000" if luminance > 0.179 else "#ffffff"


class ButtonLink(rst.Directive):
    """A simple button directive that renders a styled call-to-action button.

    Usage in myst markdown::

        ```{button-link} https://example.com
        :year: {{ year }}
        Button text
        ```

    Usage in RST::

        .. button-link:: https://example.com
           :year: {{ year }}

           Button text

    ``:year:`` picks the conference year's brand color from ``YEAR_COLORS``
    and defaults to the newest year. Conference pages have ``year`` in
    their Jinja context, so ``{{ year }}`` always matches the page.
    The text is black or white, whichever contrasts better.
    """

    required_arguments = 1  # URL
    has_content = True
    option_spec = {"year": conference_year}

    def run(self):
        url = self.arguments[0]
        text = "\n".join(self.content).strip()
        year = self.options.get("year", max(YEAR_COLORS))
        background = YEAR_COLORS[year]
        text_color = contrasting_text_color(background)
        html = f"""<div style="margin: 2em 0;">
<table border="0" cellpadding="0" cellspacing="0" style="background-color:{background}; border-radius:5px; margin:auto;">
<tr>
<td align="center" valign="middle" style="color:{text_color}; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; letter-spacing:-.5px; line-height:150%; padding-top:15px; padding-right:30px; padding-bottom:15px; padding-left:30px;">
<a href="{url}" target="_blank" style="color:{text_color}; text-decoration:none; text-transform:uppercase; border-bottom: none;">{text}</a>
</td>
</tr>
</table>
</div>"""
        return [nodes.raw("", html, format="html")]
