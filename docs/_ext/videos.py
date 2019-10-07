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


def load_conference_data():
    """
    Generate a dict with all data of all conferences including
    session details.
    """
    speakers_file_pattern = re.compile(r'(\d{4}).(\w+).speakers')
    sessions_file_pattern = re.compile(r'(\w+)-(\d{4})-day-(\d+)')
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
    return u'''{title}
{title_marker}

.. datatemplate::
   :source: /_data/{year}.{region}.speakers.yaml
   :template: videos/video-detail.html
   :key: {session_idx}

'''.format(**data)


def generate_video_listing(year, series):
    return u'''Videos of Write the Docs {series_title} {year}
=============================================================

.. toctree::
   :glob:
   :hidden:

   *

.. datatemplate::
   :source: /_data/{year}.{series}.speakers.yaml
   :template: videos/video-listing.html
'''.format(year=year, series=series, series_title=series.upper())


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
