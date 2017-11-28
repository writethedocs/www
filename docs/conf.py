# -*- coding: utf-8 -*-
#

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
import ablog
import sys
import os

sys.path.append(os.getcwd())  # noqa

from _ext.core import add_jinja_filters, rstjinja, override_page_template, load_conference_data
from _ext.meetups import MeetupListing


exclude_patterns = [
    '_build',
    'include',
    '_data',
    'conf/_cookiecutter',
    'node_modules',
]
extensions = [
    'ablog',
    'sphinxcontrib.datatemplates',
]
blog_baseurl = 'http://www.writethedocs.org/'
blog_path = 'blog/archive'
blog_authors = {
    'Team': ('Write the Docs Team', 'http://www.writethedocs.org/team/'),
    'eric': ('Eric Holscher', 'http://ericholscher.com'),
    'kelly': ("Kelly O'Brien", 'https://twitter.com/OBrienEditorial'),
}
blog_default_author = 'Team'
blog_feed_fulltext = True
blog_feed_length = 10
blog_locations = {
    'PDX': ('Portland, Oregon', 'http://www.portlandhikersfieldguide.org/'),
}
blog_default_location = 'PDX'
fontawesome_link_cdn = 'http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css'

templates_path = ['_templates']
templates_path.append(ablog.get_html_templates_path())

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
}

html_favicon = '_static/favicon/favicon-96x96.png'
html_title = 'Write the Docs'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'postcard.html',
        'info.html',
        'navigation.html',
        # 'relations.html',
        # 'searchbox.html',
    ]
}

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

suppress_warnings = ['image.nonlocal_uri']

# Our additions

html_context = {
    'conf_py_root': os.path.dirname(os.path.abspath(__file__)),
    'conferences': load_conference_data(),
}


def setup(app):
    app.connect('html-page-context', override_page_template)
    app.connect("source-read", rstjinja)
    app.connect("builder-inited", add_jinja_filters)
    app.add_directive('meetup-listing', MeetupListing)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        'enable_auto_doc_ref': True,
        'enable_eval_rst': True,
    }, True)
    app.add_transform(AutoStructify)
    app.add_stylesheet('css/global-customizations.css')
