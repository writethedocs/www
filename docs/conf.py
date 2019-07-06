# -*- coding: utf-8 -*-
#

import os
import sys

import ablog
from recommonmark.transform import AutoStructify

# Only for windows compatability - Forces default encoding to UTF8, which it may not be on windows
if os.name == 'nt':
    reload(sys)
    sys.setdefaultencoding('UTF8')


sys.path.append(os.getcwd())  # noqa

from _ext.core import (
    render_rst_with_jinja, override_template_load_context, set_html_context, unset_html_context
)
from _ext.filters import add_jinja_filters_to_app
from _ext.meetups import MeetupListing
from _ext.atom_absolute import rewrite_atom_feed

exclude_patterns = [
    '_build',
    'include',
    #'_data',
    'node_modules',
]

# Only build the videos on production, to speed up dev
on_rtd = str(os.environ.get('READTHEDOCS')).lower() == 'true'
build_videos = str(os.environ.get('BUILD_VIDEOS')).lower() == 'true'
if not on_rtd and not build_videos:
    print('EXCLUDING VIDEO PATHS. Video links will not work.')
    exclude_patterns.append('videos')
    REWRITE_FEED = False
else:
    print('BUILDING VIDEOS. All video links should work.')
    REWRITE_FEED = True

extensions = [
    'ablog',
    'sphinxcontrib.datatemplates',
    'notfound.extension',
    'recommonmark',
]
blog_baseurl = 'https://www.writethedocs.org/'
blog_path = 'blog/archive'
blog_authors = {
    'Team': ('Write the Docs Team', 'https://www.writethedocs.org/team/'),
    'eric': ('Eric Holscher', 'http://ericholscher.com'),
    'kelly': ("Kelly O'Brien", 'https://twitter.com/OBrienEditorial'),
}
blog_default_author = 'Team'
blog_feed_archives = True
blog_feed_fulltext = True
blog_feed_length = 10
blog_locations = {
    'PDX': ('Portland, Oregon', 'http://www.portlandhikersfieldguide.org/'),
}
blog_default_location = 'PDX'
fontawesome_link_cdn = 'https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css'

templates_path = ['_templates', 'include']
templates_path.append(ablog.get_html_templates_path())

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
    'sidebar_includehidden': False,
    'github_user': 'writethedocs',
    'github_repo': 'www',
    'github_banner': True,
    'github_button': False,
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
}

if build_videos:
    from _ext.videos import main

    if os.environ.get('MEETUP_API_KEY'):
        try:
            from _ext.meetup_events import main as meetup_main
            html_context.update(meetup_main())
        except:
            print('Could not get meetup events.')
    html_context.update(main())

notfound_no_urls_prefix = True


def setup(app):
    # Set up our custom jinja filters
    app.connect("builder-inited", add_jinja_filters_to_app)

    # Transform RST with Jinja, using proper context
    app.connect("source-read", render_rst_with_jinja)

    # Adjust html_context properly for datatemplate processing
    app.connect("source-read", set_html_context)
    app.connect("doctree-read", unset_html_context)

    # Render HTML templates with proper HTML context
    app.connect('html-page-context', override_template_load_context)

    if on_rtd or build_videos or REWRITE_FEED:
        app.connect('build-finished', rewrite_atom_feed)

    app.add_directive('meetup-listing', MeetupListing)
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents',
        # 'enable_auto_doc_ref': True,
        'enable_eval_rst': True,
    }, True)
    app.add_transform(AutoStructify)
    app.add_stylesheet('css/global-customizations.css')
    app.add_javascript('js/jobs.js')
