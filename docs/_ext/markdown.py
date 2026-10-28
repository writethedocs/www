"""
Fixes for Markdown pages, which MyST parses.

1. ``&`` in link URLs is escaped once, not twice.
   MyST HTML-escapes link URLs when it parses them, and Sphinx's HTML writer
   escapes them again, so ``?v=abc&list=xyz`` reaches the browser as
   ``?v=abc&amp;list=xyz`` and the second parameter is lost. Undoing MyST's
   escaping on Markdown pages leaves the writer's as the only one.

2. A ``{.class}`` line before a heading classes its whole section.
   MyST's ``attrs_block`` puts the classes on the heading itself; moving them
   to the section does what ``.. rst-class::`` does before an RST heading,
   which the front page's full-width bands rely on.
"""

import html

from docutils import nodes


def fix_markdown_doctree(app, doctree):
    if not app.env.doc2path(app.env.docname).suffix == '.md':
        return
    for ref in doctree.findall(nodes.reference):
        if '&' in ref.get('refuri', ''):
            ref['refuri'] = html.unescape(ref['refuri'])
    for section in doctree.findall(nodes.section):
        title = section.next_node(nodes.title)
        if title is not None and title.parent is section and title['classes']:
            section['classes'].extend(title['classes'])
            title['classes'] = []


def setup(app):
    # Before ablog, which copies each post's excerpt when it reads it.
    app.connect('doctree-read', fix_markdown_doctree, priority=400)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
