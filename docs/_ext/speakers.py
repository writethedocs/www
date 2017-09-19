"""
DEPRECATED
This is old transform logic that we don't need any more.

We still need to load the data,
since this was before the time of data tempaltes
"""

import os

from .core import slugify, load_yaml, load_conference_data


def main():
    """
    DEPRECATED, do not use!
    """

    conference_data = load_conference_data()
    na_2015_speakers = conference_data[2015]['na']['speakers']
    na_speakers = conference_data[2016]['na']['speakers']
    na_2017_speakers = conference_data[2017]['na']['speakers']
    na_day1 = load_yaml('_data/na-2016-day-1.yaml')
    na_day2 = load_yaml('_data/na-2016-day-2.yaml')

    eu_2017_speakers = conference_data[2017]['eu']['speakers']
    eu_speakers = conference_data[2016]['eu']['speakers']
    eu_day1 = load_yaml('_data/eu-2016-day-1.yaml')
    eu_day2 = load_yaml('_data/eu-2016-day-2.yaml')

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

    return {
        'na_2015_speakers': na_2015_speakers,
        'eu_2016_speakers': eu_speakers,
        'na_2016_speakers': na_speakers,
        'na_2017_speakers': na_2017_speakers,
        'eu_2017_speakers': eu_2017_speakers,
        'na_2016_day1': na_day1,
        'na_2016_day2': na_day2,
        'eu_2016_day1': eu_day1,
        'eu_2016_day2': eu_day2,
        'conf_py_root': os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'conferences': conference_data,
    }


def transform_speakers(speakers):
    for talk in speakers:
        for speaker in talk['speakers']:
            if os.path.exists('_static/img/speakers/%s.jpg' % speaker['slug']):
                speaker['img_file'] = '%s.jpg' % speaker['slug']
            elif os.path.exists('_static/img/speakers/%s.png' % speaker['slug']):
                speaker['img_file'] = '%s.png' % speaker['slug']
            else:
                speaker['img_file'] = 'missing.jpg'
