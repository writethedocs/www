import html

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


def render_button(url, text, year=None, wrap=True, new_tab=True, contrast=False):
    """Render a call-to-action button in the given conference year's colors.

    Used by the ``button-link`` directive and, as the ``button_link`` Jinja
    global, by the HTML templates. ``wrap`` adds vertical spacing around
    the button for use inside page content, and ``new_tab`` opens the link
    in a new tab, which page content wants and site navigation does not.
    ``contrast`` renders white on black instead, for buttons that sit on a
    brand-colored background such as the hero and footer bands.
    """
    colors = YEAR_COLORS[
        conference_year(year) if year is not None else max(YEAR_COLORS)
    ]
    if contrast:
        background, text_color = WHITE, BLACK
    else:
        background, text_color = colors["background"], colors["text"]
    target = ' target="_blank"' if new_tab else ""
    button = f"""<table border="0" cellpadding="0" cellspacing="0" style="background-color:{background}; border-radius:5px; margin:auto;">
<tr>
<td align="center" valign="middle" style="color:{text_color}; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; letter-spacing:-.5px; line-height:150%; padding-top:15px; padding-right:30px; padding-bottom:15px; padding-left:30px;">
<a href="{html.escape(url, quote=True)}"{target} style="color:{text_color}; text-decoration:none; text-transform:uppercase; border-bottom: none;">{html.escape(text)}</a>
</td>
</tr>
</table>"""
    if wrap:
        return f'<div style="margin: 2em 0;">\n{button}\n</div>'
    return button


def add_jinja_globals_to_app(app):
    """Expose ``button_link(url, text, year)`` to the HTML templates."""
    if app.builder.format != "html":
        return
    app.builder.templates.environment.globals["button_link"] = render_button


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
        rendered = render_button(url, text, self.options.get("year"))
        return [nodes.raw("", rendered, format="html")]
