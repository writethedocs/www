# Generate YAML with answers to MC questions from Pretalx
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
from collections import OrderedDict, defaultdict
from utils import slugify
import requests
from ruamel import yaml
from ruamel.yaml.representer import RoundTripRepresenter
import markdown


yamldoc = []
# Prevent OrderedDict from being presented as YAML OMAP - we just want a regular YAML dict.
yaml.add_representer(OrderedDict, RoundTripRepresenter.represent_dict, representer=RoundTripRepresenter)

def convert_to_yaml(year, series, series_slug, yaml_output, pretalx_slug):
    if not os.environ.get('PRETALX_TOKEN'):
        print('Error: PRETALX_TOKEN not found in environment variables.')
        return
    http_headers = {'Authorization': 'Token ' + os.environ['PRETALX_TOKEN']}
    submissions_url = f'https://pretalx.com/api/events/{pretalx_slug}/submissions/?state=confirmed&expand=speakers'
    print(f'Loading submissions from {submissions_url}...')
    submissions = requests.get(submissions_url, headers=http_headers)
    if submissions.status_code != 200:
        print(f'Error: submissions request failed: {submissions.status_code}: {submissions.text}')
        return

    answers = get_answers(pretalx_slug, http_headers)
    for index, talk in enumerate(submissions.json()['results']):
        slug = slugify(talk['title'] + '-' + talk['speakers'][0]['name'])
        print(f'Processing talk {slug}...')

        speaker_info = retrieve_speaker_info([s['code'] for s in talk['speakers']], http_headers, pretalx_slug, answers)
        if not speaker_info:
            print(f'Error: failed to retrieve info for speaker s["code"]')
            return

        yamldoc.append(OrderedDict([
            ('title', talk['title']),
            ('speakers', speaker_info),
        ]))

    print(f'Writing output to YAML file {yaml_output}')
    yaml_obj = yaml.YAML(typ='safe')
    yaml_obj.Representer = RoundTripRepresenter
    yaml_obj.default_flow_style = False
    with open(yaml_output, 'w+') as yaml_file:
        yaml_obj.dump(yamldoc, yaml_file)
    print('Completed!')


def retrieve_speaker_info(speaker_codes, http_headers, pretalx_slug, answers):
    result = []
    for speaker_code in speaker_codes:
        speaker_url = f'https://pretalx.com/api/events/{pretalx_slug}/speakers/{speaker_code}/?questions=all'
        print(f'Loading speaker info from {speaker_url}...')
        speaker_response = requests.get(speaker_url, headers=http_headers)
        if speaker_response.status_code != 200:
            print(f'Error: speaker request failed: {speaker_response.status_code}: {speaker_response.text}')
            return

        def search_answers(speaker_dict, search_string):
            for question, answer in answers.get(speaker_code, []):
                if search_string in question.lower():
                    return answer

        speaker = speaker_response.json()

        result.append(OrderedDict([
            ('name', speaker['name']),
            ('email', speaker['email']),
            ('pronouns', search_answers(speaker, 'do you use')),
            ('bio', search_answers(speaker, 'short bio')),
            ('pronounce', search_answers(speaker, 'pronounce')),
            #('slack', search_answers(speaker, 'slack')),
            #('li', search_answers(speaker, 'linkedin')),
            #('shirt', search_answers(speaker, 'shirt')),

        ]))
    return result


def get_answers(pretalx_slug, http_headers):
    url = f'https://pretalx.com/api/events/{pretalx_slug}/answers/?expand=question'
    print(f'Loading answers from {url}...')
    answers = load_pretalx_resource(url, http_headers)
    result = defaultdict(list)
    for answer in answers:
        result[answer['person']].append((answer['question']['question']['en'], answer['answer']))
    return result

def load_pretalx_resource(url, http_headers):
    results = []
    while url:
        response = requests.get(url, headers=http_headers)
        # 403 may occur as a pretalx bug
        if response.status_code not in [200, 403]:
            print(f'Error: request failed: {response.status_code}: {response.text}')
            return

        results += response.json()['results']

        if response.json()['next']:
            url = response.json()['next']
        else:
            break
    return results


if __name__ == '__main__':
    convert_to_yaml(
        year='2025',
        series='Write the Docs Portland',
        series_slug='portland',
        yaml_output='../_data/mc-info.yaml',
        pretalx_slug='wtd-portland-2025'
    )
