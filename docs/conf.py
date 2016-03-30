# -*- coding: utf-8 -*-
#
import sys
import os
import shlex
import shutil
import json
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
primary_domain = None

html_theme = 'alabaster'
html_theme_options = {
    'logo': 'sticker-wtd-colors.png',
    'github_button': False,
    'sidebar_includehidden': False,
    # 'show_related': True,
    # 'github_user': 'writethedocs',
    # 'github_repo': 'www',
}

html_favicon = '_static/img/favicon.ico'
html_title = 'Write the Docs'
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

speakers = json.load(file('data/2016.speakers.json'))

for talk in speakers:
    for speaker in talk['speakers']:
        if os.path.exists('_static/img/speakers/%s.jpg' % speaker['slug']):
            speaker['img_file'] = '%s.jpg' % speaker['slug']
        else:
            speaker['img_file'] = 'missing.jpg'

html_context = {
    'speakers2016': speakers
}


def on_page_context(app, pagename, templatename, context, doctree):
    # Markdown
    if (context and
            'page_source_suffix' in context and
            context['page_source_suffix'] == '.md'):
        txt = doctree[0].astext()
        if txt.startswith(':template:'):
            context['body'] = context['body'].replace(txt, '')
            return txt.split(':')[2].strip()
        else:
            print "Unknown context %s" % pagename
    # rst
    try:  # Sphinx was throwing a weird error here, and this is a workaround
        if (context and
                'meta' in context and
                'template' in context.get('meta', {})):
            return context['meta']['template']
    except TypeError:
        pass


def rstjinja(app, docname, source):
    """
    Render the speaker page as a template.
    """
    if docname.startswith('conf/na/2016/'):
        src = source[0]
        rendered = app.builder.templates.render_string(src, app.config.html_context)
        source[0] = rendered


def setup(app):
    app.add_stylesheet('writethedocs.css')
    app.connect('html-page-context', on_page_context)
    app.connect("source-read", rstjinja)

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
