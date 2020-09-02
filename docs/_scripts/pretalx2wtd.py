# Generate a sessions YAML from Pretalx talk selections.
# To use:
# - Get an API token from https://pretalx.com/orga/me
# - Update the parameters at the end of this file, if needed (e.g. conference name)
# - Do: export PRETALX_TOKEN=<your token>
# - Go to directory docs/_scripts
# - Run this script
import shutil
import sys
sys.path.insert(1, '../_ext')

import os
from collections import OrderedDict
from utils import slugify
import requests
from ruamel import yaml
from ruamel.yaml.representer import RoundTripRepresenter
import markdown

SPEAKER_IMAGE_PATH = '../_static/img/speakers/'

yamldoc = []
# Prevent OrderedDict from being presented as YAML OMAP - we just want a regular YAML dict.
yaml.add_representer(OrderedDict, RoundTripRepresenter.represent_dict, representer=RoundTripRepresenter)


def convert_to_yaml(year, series, series_slug, yaml_output, pretalx_slug):
    if not os.environ.get('PRETALX_TOKEN'):
        print('Error: PRETALX_TOKEN not found in environment variables.')
        return
    http_headers = {'Authorization': 'Token ' + os.environ['PRETALX_TOKEN']}
    submissions_url = f'https://pretalx.com/api/events/{pretalx_slug}/submissions/?state=confirmed'
    print(f'Loading submissions from {submissions_url}...')
    submissions = requests.get(submissions_url, headers=http_headers)
    if submissions.status_code != 200:
        print(f'Error: submissions request failed: {submissions.status_code}: {submissions.text}')
        return

    for index, talk in enumerate(submissions.json()['results']):
        slug = slugify(talk['title'] + '-' + talk['speakers'][0]['name'])
        print(f'Processing talk {slug}...')

        speaker_info = retrieve_speaker_info([s['code'] for s in talk['speakers']], http_headers, pretalx_slug)
        if not speaker_info:
            print(f'Error: failed to retrieve info for speaker s["code"]')
            return

        yamldoc.append(OrderedDict([
            ('title', talk['title']),
            ('slug', slug),
            ('series', series),
            ('series_slug', series_slug),
            ('year', int(year)),
            ('speakers', speaker_info),
            ('abstract', markdown.markdown(talk['abstract'])),
        ]))

    print(f'Writing output to YAML file {yaml_output}')
    yaml_obj = yaml.YAML(typ='safe')
    yaml_obj.Representer = RoundTripRepresenter
    yaml_obj.default_flow_style = False
    with open(yaml_output, 'w+') as yaml_file:
        yaml_obj.dump(yamldoc, yaml_file)
    print('Completed!')


def retrieve_speaker_info(speaker_codes, http_headers, pretalx_slug):
    result = []
    for speaker_code in speaker_codes:
        speaker_url = f'https://pretalx.com/api/events/{pretalx_slug}/speakers/{speaker_code}/'
        print(f'Loading speaker info from {speaker_url}...')
        speaker_response = requests.get(speaker_url, headers=http_headers)
        if speaker_response.status_code != 200:
            print(f'Error: speaker request failed: {speaker_response.status_code}: {speaker_response.text}')
            return

        def search_answers(speaker_dict, search_string):
            for answer in speaker_dict['answers']:
                if search_string in answer['question']['question']['en'].lower():
                    return answer['answer']

        speaker = speaker_response.json()
        speaker_slug = slugify(speaker['name'])

        if speaker['avatar']:
            avatar_path = SPEAKER_IMAGE_PATH + speaker_slug + '.' + speaker['avatar'].split('.')[-1].lower().replace('jpeg', 'jpg')
            image_response = requests.get(speaker['avatar'], stream=True)
            if image_response.status_code != 200:
                print(f'Error: speaker avatar request failed: {image_response.status_code}: {image_response.text}')
                return
            with open(avatar_path, 'wb') as f:
                image_response.raw.decode_content = True
                shutil.copyfileobj(image_response.raw, f)
            print(f'Saved speaker photo to {avatar_path}')

        result.append(OrderedDict([
            ('name', speaker['name']),
            ('slug', speaker_slug),
            ('twitter', search_answers(speaker, 'twitter')),
            ('website', search_answers(speaker, 'website')),
        ]))
    return result

if __name__ == '__main__':
    convert_to_yaml(
        year='2020',
        series='Write the Docs Prague',
        series_slug='prague',
        yaml_output='../_data/prague-2020-sessions.yaml',
        pretalx_slug='wtd-prague-2020'
    )
