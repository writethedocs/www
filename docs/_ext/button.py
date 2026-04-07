from docutils import nodes
from docutils.parsers import rst


class ButtonLink(rst.Directive):
    """A simple button directive that renders a styled call-to-action button.

    Usage in myst markdown::

        ```{button-link} https://example.com
        Button text
        ```

    Usage in RST::

        .. button-link:: https://example.com

           Button text
    """

    required_arguments = 1  # URL
    has_content = True

    def run(self):
        url = self.arguments[0]
        text = "\n".join(self.content).strip()
        html = f"""<div style="margin: 2em 0;">
<table border="0" cellpadding="0" cellspacing="0" style="background-color:#fdb913; border-radius:5px; margin:auto;">
<tr>
<td align="center" valign="middle" style="color:#000000; font-family:Helvetica, Arial, sans-serif; font-size:16px; font-weight:bold; letter-spacing:-.5px; line-height:150%; padding-top:15px; padding-right:30px; padding-bottom:15px; padding-left:30px;">
<a href="{url}" target="_blank" style="color:#000000; text-decoration:none; text-transform:uppercase; border-bottom: none;">{text}</a>
</td>
</tr>
</table>
</div>"""
        return [nodes.raw("", html, format="html")]
