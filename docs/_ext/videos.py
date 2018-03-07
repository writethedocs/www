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

    for year, regions in conference_data.items():
        for region, data in regions.items():
            index_path = os.path.join('videos', region, unicode(year))
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
                print('Generated {}.rst'.format(video_path))

    return {
        'conf_py_root': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'conferences': conference_data,
    }
