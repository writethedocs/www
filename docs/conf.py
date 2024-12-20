# -*- coding: utf-8 -*-
#

import os
import sys

import yaml
import ablog

# Only for windows compatibility - Forces default encoding to UTF8, which it may not be on windows
if os.name == 'nt':
    # monkeypatches sphinxcontrib.datatemplates so it uses utf-8 as the encoding
    # instead of cp1252 when opening a file. using sys.setdefaultencoding does
    # not alter the encoding when opening a file for reading.

    from sphinxcontrib.datatemplates import directive
    from xml.etree import ElementTree as ET
    import mimetypes

    old_load_data = directive.DataTemplateLegacy._load_data

    def _load_data(self, env, data_source, encoding):
        rel_filename, filename = env.relfn2path(data_source)
        if data_source.endswith('.yaml'):
            return self._load_yaml(filename, 'utf-8')
        elif data_source.endswith('.json'):
            return self._load_json(filename, 'utf-8')
        elif data_source.endswith('.csv'):
            return self._load_csv(filename, 'utf-8')
        elif "xml" in mimetypes.guess_type(data_source)[0]:
            # there are many XML based formats
            return ET.parse(filename).getroot()
        else:
            raise NotImplementedError('cannot load file type of %s' %
                                      data_source)


    directive.DataTemplateLegacy._load_data = _load_data
    setattr(
        sys.modules['sphinxcontrib.datatemplates.directive'].DataTemplateLegacy,
        '_load_data',
        _load_data
    )


sys.path.append(os.getcwd())  # noqa


# Updates for RTD changes
# https://about.readthedocs.com/blog/2024/07/addons-by-default/

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "https://www.writethedocs.org")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True


from _ext.core import (
    render_rst_with_jinja, override_template_load_context, set_html_context, unset_html_context
)
from _ext.filters import add_jinja_filters_to_app
from _ext.meetups import MeetupListing
from _ext.atom_absolute import rewrite_atom_feed
from _ext import videos

exclude_patterns = [
    '_build',
    'include',
    #'_data',
    'node_modules',
    'videos/prague/2018/tackling-technical-debt-in-the-docs-louise-fahey.rst',
]

# We use these *local* environment variables for private info like free ticket links

cfp_variables = {}
cfp_variables['upload'] = os.environ.get('WTD_CFP_UPLOAD')
cfp_variables['ticket'] = os.environ.get('WTD_CFP_SPEAKER_TICKET')
cfp_variables['calendly'] = os.environ.get('WTD_CFP_CALENDLY')
cfp_variables['feedback_form'] = os.environ.get('WTD_CFP_FEEDBACK_FORM')
cfp_variables['speaker_gift_form'] = os.environ.get('WTD_CFP_SPEAKER_GIFT_FORM')

if all(cfp_variables.values()):
    print('Private CFP environment variables set. ✅')
    cfp_variables['print_templates'] = True
else:
    print('Private CFP environment variables not set, not building CFP email templates.')

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
    'sphinxemoji.sphinxemoji',
    'myst_parser',
    'sphinxext.opengraph',
]

myst_heading_anchors = 4


ogp_site_name = "Write the Docs"
ogp_site_url = "/"
ogp_image = 'https://www.writethedocs.org/_static/logo-opengraph.png'
ogp_use_first_image = True
ogp_enable_meta_description = True
# Inspired by https://github.com/executablebooks/MyST-Parser/pull/404/
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" />',
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
# Only show 1 blog so we don't overload Mailchimp
blog_feed_length = 1
blog_locations = {
    'PDX': ('Portland, Oregon', 'http://www.portlandhikersfieldguide.org/'),
}
blog_default_location = None
fontawesome_link_cdn = 'https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css'

templates_path = ['_templates', 'include', ablog.get_html_templates_path()]
html_extra_path = ['_static_html']
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
html_copy_source = False
html_sidebars = {
    '**': [
        'about.html',
        'postcard.html',
        'info.html',
        'searchbox.html',
        'navigation.html',
        # 'relations.html',
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

global_sponsors = yaml.safe_load("""
- name: gitbook
  link: https://www.gitbook.com/?utm_campaign=launch&utm_medium=display&utm_source=write_the_docs&utm_content=ad
  brand: GitBook
  comment: Community sponsor
""")

html_context = {
    'conf_py_root': os.path.dirname(os.path.abspath(__file__)),
    'newsletter_subs': '10,000',
    'slack_members': '22,500',
    'website_visits': '20,000',
    'global_sponsors': global_sponsors,
    'cfp_variables': cfp_variables,
    'slack_join': "https://join.slack.com/t/writethedocs/shared_invite/zt-2le6owut0-0WqJ3z5dtQyrIerk97YNlw",
    'slack_form': "https://docs.google.com/forms/d/e/1FAIpQLSdq4DWRphVt1qVqH8NsjNnS0Szu_NljjZRUvyYqR7mdc00zKQ/viewform?usp=sf_link",
}

if build_videos:

    html_context.update(videos.main())

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
    app.add_directive('datatemplate-video', videos.DataTemplateVideo)
    app.add_css_file('css/global-customizations.css')
    app.add_css_file('css/survey.css')

    app.config.wtd_cache = {}
