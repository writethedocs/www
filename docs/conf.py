# -*- coding: utf-8 -*-
#
import CommonMark
import collections
import glob
import io
import os
import json
import re
import os.path
import yaml
import shutil

from docutils.parsers import rst
from docutils import nodes
from docutils.statemachine import ViewList
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from sphinx.util.nodes import nested_parse_with_titles
import ablog

try:
    # Python 2.6-2.7 
    from HTMLParser import HTMLParser
except ImportError:
    # Python 3
    from html.parser import HTMLParser


exclude_patterns = [
    '_build',
    'include',
    '_data',
]
extensions = [
    'ablog',
    'sphinxcontrib.datatemplates',
]
blog_baseurl = 'http://www.writethedocs.org/blog/'
blog_path = 'blog/archive'
blog_authors = {
    'Team': ('Write the Docs Team', 'http://www.writethedocs.org/team/'),
    'eric': ('Eric Holscher', 'http://ericholscher.com'),
    'kelly': ("Kelly O'Brien", 'https://twitter.com/OBrienEditorial'),
}
blog_default_author = 'Team'

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

html_favicon = '_static/img/favicon.ico'
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


# Our fancy additions

def slugify(slug):
    slug = slug.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def transform_speakers(speakers):
    for talk in speakers:
        for speaker in talk['speakers']:
            if os.path.exists('_static/img/speakers/%s.jpg' % speaker['slug']):
                speaker['img_file'] = '%s.jpg' % speaker['slug']
            elif os.path.exists('_static/img/speakers/%s.png' % speaker['slug']):
                speaker['img_file'] = '%s.png' % speaker['slug']
            else:
                speaker['img_file'] = 'missing.jpg'


def load_yaml(path):
    with io.open(path, encoding='utf-8') as fp:
        return yaml.safe_load(fp)

def load_meetups_by_region():
    result = collections.defaultdict(list)
    for yaml_file in glob.glob('_data/meetups/*.yaml'):
        meetup = load_yaml(yaml_file)
        if not 'website' in meetup:
            raise SphinxError('Meetup needs a website')
        result[meetup['region']].append(meetup)
    for _, meetups in result.items():
        meetups.sort(key=lambda m : m.get('city', m['country']))
    return result

def normalize_session(session):
    youtube_pattern = re.compile(r'https://www.youtube.com/watch\?v=(.+)')

    session['slug'] = generate_video_slug(session)
    if 'video' in session and 'youtube.com' in session['video']:
        mo = youtube_pattern.match(session['video'])
        if mo:
            session['youtubeId'] = mo.group(1)

def load_conference_data():
    speakers_file_pattern = re.compile(r'(\d{4}).(\w+).speakers')
    sessions_file_pattern = re.compile(r'(\w+)-(\d{4})-day-(\d+)')
    result = {}
    # result = collections.defaultdict(lambda : collections.defaultdict(collections.defaultdict))
    for f in glob.glob('_data/*.yaml'):
        base = os.path.basename(f)
        base, _ = os.path.splitext(base)
        # Only consider conference data files that are following the common
        # naming convention and log everything out as warning.
        mo = speakers_file_pattern.match(base)
        if mo:
            year = int(mo.group(1))
            region = mo.group(2)
            if year not in result:
                result[year] = {}
            if region not in result[year]:
                result[year][region] = {}
            result[year][region]['speakers'] = load_yaml(f)
            for session in result[year][region]['speakers']:
                normalize_session(session)
                session['year'] = year
                session['series'] = u'Write the Docs {}'.format(region.upper())
                session['series_slug'] = region
                session['event'] = u'Write the Docs {} {}'.format(region.upper(), year)
                session['path'] = 'conf/{series_slug}/{year}/videos/{slug}'.format(**session)
            continue
        mo = sessions_file_pattern.match(base)
        if mo:
            continue
        print("%s doesn't follow the conference data file conventions" % (base,))
    return result

def generate_video_slug(session):
    title = session['title']
    for speaker in session.get('speakers', []):
        title += '-{}'.format(speaker.get('slug', speaker['name']))
    return slugify(title)

def generate_video_content(session, year, region, session_idx):
    data = session.copy()
    data['title_marker'] = u'=' * len(data['title'])
    data['year'] = year
    data['region'] = region
    data['session_idx'] = session_idx
    return u''':template: 2017/video-details.html

{title}
{title_marker}

{{% set talk = conferences[{year}]['{region}']['speakers'][{session_idx}] %}}
{{% set output %}}
{{% include conf_py_root + '/_templates/video-details-body.html' %}}
{{% endset %}}
.. raw:: html

    {{{{ output|indent(4) }}}}
'''.format(**data)


def generate_videolisting_by_year(year):
    return u''':template: 2017/conference-videos-archive.html

Videos of {year}
==============

{{% set output %}}
{{% set path_to_root = '../../..' %}}
{{% set talks = sessions_by_year[{year}] %}}
{{% include conf_py_root + "/_templates/video-listing.html" %}}
{{% endset %}}

.. raw:: html
   
   {{{{ output|indent(3) }}}}

'''.format(year=year)

def generate_videolisting_by_series(series):
    return u''':template: 2017/conference-videos-archive.html

Videos from Write the Docs {series_title}
=============================================

{{% set output %}}
{{% set talks = sessions_by_series['{series}'] %}}
{{% set path_to_root = '../../..' %}}
{{% include conf_py_root + "/_templates/video-listing.html" %}}
{{% endset %}}

.. raw:: html
   
   {{{{ output|indent(3) }}}}

'''.format(series=series, series_title=series.upper())

conference_data = load_conference_data()
sessions_by_year = {}
sessions_by_series = {}
shutil.rmtree(os.path.join('videos', 'by-year'), ignore_errors=True)
shutil.rmtree(os.path.join('videos', 'by-series'), ignore_errors=True)
os.makedirs(os.path.join('videos', 'by-year'))
os.makedirs(os.path.join('videos', 'by-series'))
for year, regions in conference_data.items():
    year_path = os.path.join('videos', 'by-year', unicode(year))
    sessions_by_year[year] = []
    with io.open(year_path + '.rst', 'w') as fp:
        print('Generated {}.rst'.format(year_path + '.rst'))
        fp.write(generate_videolisting_by_year(year))
    for region, data in regions.items():
        if region not in sessions_by_series:
            sessions_by_series[region] = []
        index_path = os.path.join('conf', region, unicode(year), 'videos')
        shutil.rmtree(index_path, ignore_errors=True)
        os.makedirs(index_path)
        for idx, speaker in enumerate(data['speakers']):
            video_slug = generate_video_slug(speaker)
            video_path = os.path.join(index_path, video_slug)
            video_content = generate_video_content(speaker, year, region, idx)
            with io.open(video_path + '.rst', 'w+') as fp:
                fp.write(video_content)
            sessions_by_year[year].append(speaker)
            sessions_by_series[region].append(speaker)
            print('Generated {}.rst'.format(video_path))
for series in sessions_by_series.keys():
    series_file = os.path.join('videos', 'by-series', '{}.rst'.format(series))
    with io.open(series_file, 'w+') as fp:
        fp.write(generate_videolisting_by_series(series))
    print('Generated {}'.format(series_file))

na_2015_speakers = conference_data[2015]['na']['speakers']
na_speakers = conference_data[2016]['na']['speakers']
na_2017_speakers = conference_data[2017]['na']['speakers']
na_day1 = load_yaml('_data/na-2016-day-1.yaml')
na_day2 = load_yaml('_data/na-2016-day-2.yaml')

eu_2017_speakers = conference_data[2017]['eu']['speakers']
eu_speakers = conference_data[2016]['eu']['speakers']
eu_day1 = load_yaml('_data/eu-2016-day-1.yaml')
eu_day2 = load_yaml('_data/eu-2016-day-2.yaml')

meetups_by_region = load_meetups_by_region()

for list_o_speakers in [na_speakers, eu_speakers, na_2017_speakers, eu_2017_speakers]:
    transform_speakers(list_o_speakers)

for talk in na_day1 + na_day2:
    # Old NA hacks
    if 'Tim Nugent' in talk['Session']:
        talk['speaker'] = 'Tim Nugent'
        talk['slug'] = 'tim-nugent'
    else:
        speaker = talk['Session'].split('-')[-1]
        speaker = speaker.split(',')[0]
        speaker = speaker.split('&')[0]
        talk['speaker'] = speaker.strip()
        slug = slugify(speaker)
        talk['slug'] = slug.strip()

for talk in eu_day1 + eu_day2:
    speaker = talk['Session'].split('-')[0]
    speaker = speaker.split(',')[0]
    speaker = speaker.split('&')[0]
    talk['speaker'] = speaker.strip()
    slug = slugify(speaker)
    talk['slug'] = slug.strip()

    # slug hacks
    if 'Kata' in talk['Session']:
        talk['slug'] = 'kata-nagygyorgy'
    if 'native speaker' in talk['Session']:
        talk['slug'] = 'istvan-zoltan-szabo'


html_context = {
    'na_2015_speakers': na_2015_speakers,
    'eu_2016_speakers': eu_speakers,
    'na_2016_speakers': na_speakers,
    'na_2017_speakers': na_2017_speakers,
    'eu_2017_speakers': eu_2017_speakers,
    'na_2016_day1': na_day1,
    'na_2016_day2': na_day2,
    'eu_2016_day1': eu_day1,
    'eu_2016_day2': eu_day2,
    'conf_py_root': os.path.dirname(os.path.abspath(__file__)),
    'meetups_by_region': meetups_by_region,
    'conferences': conference_data,
    'sessions_by_year': sessions_by_year,
    'sessions_by_series': sessions_by_series,
}

state_abbreviations = {
    'Canada': {
        'Ontario': 'ON',
    },
    'USA': {
        'California': 'CA',
        'Colorado': 'CO',
        'Idaho': 'ID',
        'Massachusetts': 'MA',
        'New York': 'NY',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Texas': 'TX',
        'Washington': 'WA',
    }
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
    Render our conf pages as a jinja template for more goodness.
    """
    if getattr(app.builder, 'implementation', None) or app.builder.format != 'html':
        return
    if docname.startswith(('conf/', 'guide/', 'videos/by-year', 'videos/by-series')):
        src = source[0]
        rendered = app.builder.templates.render_string(src, app.config.html_context)
        source[0] = rendered


def add_jinja_filters(app):
    if getattr(app.builder, 'implementation', None) or app.builder.format != 'html':
        return
    def markdown_filter(data):
        parser = CommonMark.DocParser()
        renderer = CommonMark.HTMLRenderer()
        return renderer.render(parser.parse(data))
    def state_abbr(meetup):
        states = state_abbreviations.get(meetup['country'])
        if not states:
            return meetup['state']
        return states.get(meetup['state'], meetup['state'])
    def html_unescape(str):
        h = HTMLParser()
        return h.unescape(str)
    app.builder.templates.environment.filters['markdown'] = markdown_filter
    app.builder.templates.environment.filters['html_unescape'] = html_unescape
    app.builder.templates.environment.filters['state_abbr'] = state_abbr
    app.builder.templates.environment.filters['slugify'] = slugify


class MeetupListing(rst.Directive):
    option_spec = {
        'region': rst.directives.unchanged,
    }
    has_content = False

    def run(self):
        env = self.state.document.settings.env
        app = env.app
        builder = app.builder

        templates = getattr(builder, 'templates', None)
        if not templates:
            return []

        region_name = self.options['region']
        output = ViewList()
        template_name = 'include/meetups/listing.jinja'
        rendered = builder.templates.render(template_name, {
            'meetups': meetups_by_region[region_name],
        })
        for line in rendered.splitlines():
            output.append(line, 'meetup-data')
        node = nodes.section()
        node.document = self.state.document
        nested_parse_with_titles(self.state, output, node)
        return node.children


def setup(app):
    app.connect('html-page-context', on_page_context)
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
