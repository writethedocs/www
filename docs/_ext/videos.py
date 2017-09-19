"""
Video archive creator

Create new videos by adding the following to ``conf.py``::

    from ._ext.videos import main

    html_context.update(main())
"""

import io
import os
import os.path
import shutil

from .core import generate_video_slug, load_conference_data


def generate_video_content(session, year, region, session_idx):
    data = session.copy()
    if 'title' not in session:
        return u''
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


def main():
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

    return {
        'sessions_by_year': sessions_by_year,
        'sessions_by_series': sessions_by_series,
        'conf_py_root': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'conferences': conference_data,
    }
