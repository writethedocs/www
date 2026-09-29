import re

from docutils import nodes
from docutils.parsers import rst

# Brand color of the current conference year. Older years pass ``:color:``.
DEFAULT_COLOR = "#fdb913"

HEX_COLOR_RE = re.compile(r"^#?(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def hex_color(argument):
    """Validate a ``#rgb`` or ``#rrggbb`` option value.

    In Markdown the value must be quoted (``:color: "#fdb913"``), because
    MyST reads directive options as YAML and an unquoted ``#`` starts a
    comment.
    """
    value = (argument or "").strip()
    if not HEX_COLOR_RE.match(value):
        raise ValueError(
            f'expected a hex color like "#fdb913" (quote it in Markdown), got {value!r}'
        )
    return "#" + value.lstrip("#").lower()


def contrasting_text_color(background):
    """Return black or white, whichever reads better on ``background``."""
    hex_digits = background.lstrip("#")
    if len(hex_digits) == 3:
        hex_digits = "".join(digit * 2 for digit in hex_digits)
    red, green, blue = (int(hex_digits[i : i + 2], 16) / 255 for i in (0, 2, 4))

    def linear(channel):
        if channel <= 0.03928:
            return channel / 12.92
        return ((channel + 0.055) / 1.055) ** 2.4

    luminance = 0.2126 * linear(red) + 0.7152 * linear(green) + 0.0722 * linear(blue)
    return "#000000" if luminance > 0.179 else "#ffffff"


class ButtonLink(rst.Directive):
    """A simple button directive that renders a styled call-to-action button.

    Usage in myst markdown::

        ```{button-link} https://example.com
        :color: "#2ecc71"
        Button text
        ```

    Usage in RST::

        .. button-link:: https://example.com
           :color: #2ecc71

           Button text

    ``:color:`` sets the button background and defaults to the current
    year's brand color. The text is black or white, whichever contrasts
    better, unless ``:text-color:`` overrides it.
    """

    required_arguments = 1  # URL
    has_content = True
    option_spec = {
        "color": hex_color,
        "text-color": hex_color,
    }

    def run(self):
        url = self.arguments[0]
        text = "\n".join(self.content).strip()
        background = self.options.get("color", DEFAULT_COLOR)
        text_color = self.options.get("text-color") or contrasting_text_color(background)
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
