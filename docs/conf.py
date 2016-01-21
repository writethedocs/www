# -*- coding: utf-8 -*-
#
import sys
import os
import shlex
import shutil
from recommonmark.parser import CommonMarkParser

exclude_patterns = ['_build', 'include']
extensions = []
templates_path = ['_templates']
source_parsers = {
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']
master_doc = 'index'
project = u'Write the Docs'
copyright = u'2016, The Write the Docs Community'
author = u'The Write the Docs Community'
version = '1.0'
release = '1.0'
language = 'en'
html_search_language = 'en'
pygments_style = 'sphinx'

html_theme = 'alabaster'
html_theme_options = {
    'logo': 'sticker-wtd-colors.png',
    'github_button': False,
    # 'show_related': True,
    # 'github_user': 'writethedocs',
    # 'github_repo': 'www',
}

html_title = 'Write the Docs'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

html_static_path = ['_static']

html_sidebars = {
    '**': [
        'about.html',
        'info.html',
        'navigation.html',
        # 'relations.html',
        # 'searchbox.html',
    ]
}


def on_page_context(app, pagename, templatename, context, doctree):
    # Markdown
    if 'page_source_suffix' in context and context['page_source_suffix'] == '.md':
        txt = doctree[0].astext()
        if txt.startswith(':template:'):
            import ipdb; ipdb.set_trace()
            context['body'] = context['body'].replace(txt, '')
            return txt.split(':')[2].strip()
    # Sphinx
    if context and 'meta' in context and 'template' in context.get('meta', {}):
        return context['meta']['template']


def on_source_read(app, docname, source):
    src = source[0]
    if hasattr(app.builder, 'globalcontext'):
        app.info('Using global context')
        source[0] = app.builder.templates.render_string(src, app.builder.globalcontext)
    else:
        source[0] = app.builder.templates.render_string(src, {})


def setup(app):
    # app.connect("source-read", on_source_read)
    app.add_stylesheet('writethedocs.css')
    app.connect('html-page-context', on_page_context)

# Output formats

htmlhelp_basename = 'WritetheDocsdoc'

latex_documents = [
    (master_doc, 'WritetheDocs.tex', u'Write the Docs Documentation',
     u'Eric Holscher \\& the Write the Docs Community', 'manual'),
]

man_pages = [
    (master_doc, 'writethedocs', u'Write the Docs Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'WritetheDocs', u'Write the Docs Documentation',
     author, 'WritetheDocs', 'One line description of project.',
     'Miscellaneous'),
]
