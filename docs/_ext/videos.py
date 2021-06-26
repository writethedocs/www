"""
Video archive creator

Create new videos by adding the following to ``conf.py``::

    from ._ext.videos import main

    html_context.update(main())
"""
from __future__ import print_function

import glob
import re

from builtins import str
import io
import os
import os.path

from _ext.utils import generate_video_slug, load_yaml, normalize_session
from docutils.parsers import rst
from sphinxcontrib.datatemplates.directive import DataTemplateYAML


def load_conference_data():
    """
    Generate a dict with all data of all conferences including
    session details.
    """
    # Speakers are the legacy format, >=2020 conferences have a sessions file
    speakers_file_pattern = re.compile(r'(\d{4}).(\w+).speakers')
    sessions_file_pattern = re.compile(r'(\w+)-(\d{4})-sessions')
    result = {}
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
            region = mo.group(1)
            year = int(mo.group(2))
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
    return result


def generate_video_content(session, year, region, session_idx):
    data = session.copy()
    if 'title' not in session:
        return u''
    data['title_marker'] = u'=' * len(data['title'])
    data['year'] = year
    data['region'] = region
    data['session_idx'] = session_idx

    data['data_file'] = f'/_data/{year}.{region}.speakers.yaml' if year < 2020 else f'/_data/{region}-{year}-sessions.yaml'
    return u'''{title}
{title_marker}

.. datatemplate-video::
   :source: {data_file}
   :template: videos/video-detail.html
   :key: {session_idx}

'''.format(**data)


def generate_video_listing(year, series):
    data_file = f'/_data/{year}.{series}.speakers.yaml' if year < 2020 else f'/_data/{series}-{year}-sessions.yaml'
    return u'''Videos of Write the Docs {series_title} {year}
=============================================================

.. toctree::
   :glob:
   :hidden:

   *

.. datatemplate::
   :source: {data_file}
   :template: videos/video-listing.html
'''.format(year=year, series=series, series_title=series.upper(), data_file=data_file)


def main():
    conference_data = load_conference_data()

    for year, regions in list(conference_data.items()):
        for region, data in list(regions.items()):
            has_videos = False
            for speaker in data['speakers']:
                if speaker.get('youtubeId'):
                    has_videos = True
                    break

            if not has_videos:
                continue

            index_path = os.path.join('videos', region, str(year))
            if not os.path.exists(index_path):
                os.makedirs(index_path)
            with io.open(os.path.join(index_path, 'index.rst'), 'w+') as fp:
                fp.write(generate_video_listing(year, region))

            for idx, speaker in enumerate(data['speakers']):
                video_slug = generate_video_slug(speaker)
                video_path = os.path.join(index_path, video_slug)
                video_content = generate_video_content(speaker, year, region, idx)
                with io.open(video_path + '.rst', 'w+') as fp:
                    fp.write(video_content)

    return {
        'conf_py_root': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'conferences': conference_data,
    }


class DataTemplateVideo(DataTemplateYAML):
    option_spec = dict(DataTemplateYAML.option_spec, **{
        'key': rst.directives.nonnegative_int,
    })

    def _make_context(self, data, config, env):
        context = super()._make_context(data, config, env)
        context['key'] = self.options.get('key')
        return context
