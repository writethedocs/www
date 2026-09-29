from docutils import nodes
from docutils.parsers import rst

# Brand color of each conference year, matching $main-color in
# docs/_static/conf/scss/main-<year>.scss, and the text color that reads
# well on it.
BLACK = "#000000"
WHITE = "#ffffff"
YEAR_COLORS = {
    2018: {"background": "#3dd94a", "text": BLACK},
    2019: {"background": "#ea7852", "text": BLACK},
    2020: {"background": "#3498db", "text": BLACK},
    2021: {"background": "#fdb913", "text": BLACK},
    2022: {"background": "#2ecc71", "text": BLACK},
    2023: {"background": "#ea7852", "text": BLACK},
    2024: {"background": "#4ac1e0", "text": BLACK},
    2025: {"background": "#2ecc71", "text": BLACK},
    2026: {"background": "#fdb913", "text": BLACK},
    2027: {"background": "#ea6852", "text": BLACK},
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

    ``:year:`` picks the conference year's colors from ``YEAR_COLORS``
    and defaults to the newest year. Conference pages have ``year`` in
    their Jinja context, so ``{{ year }}`` always matches the page.
    """

    required_arguments = 1  # URL
    has_content = True
    option_spec = {"year": conference_year}

    def run(self):
        url = self.arguments[0]
        text = "\n".join(self.content).strip()
        year = self.options.get("year", max(YEAR_COLORS))
        colors = YEAR_COLORS[year]
        background = colors["background"]
        text_color = colors["text"]
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
