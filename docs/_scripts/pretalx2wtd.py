import sys
sys.path.insert(1, '../_ext')

from utils import slugify
import json
from ruamel.yaml import YAML

yamldoc = []

def convert_to_yaml(year, series, slug, pretalx_results, yaml_file):
    with open(pretalx_results) as json_file:
        talks = json.load(json_file)
        for index, talk in enumerate(talks['results']):
            yamldoc.append({
                'title': talk['title'],
                'slug':slugify(talk['title'] + '-' + talk['speakers'][0]['name']),
                'abstract': talk['abstract'],
                'speakers': [],
                'series': series,
                'series_slug': slug,
                'year': int(year)

                })
            for s in talk['speakers']:
                yamldoc[index]['speakers'].append({
                    'name': s['name'],
                    'slug': slugify(s['name']),
                    'avatar': s['avatar']
                     })

        yaml=YAML(typ='safe')
        yaml.default_flow_style = False
        yaml.dump(yamldoc, open(yaml_file, 'w+'))



if __name__ == '__main__':
    convert_to_yaml('2020', 'Write the Docs Portland', 'portland', 'talks.json', '../_data/portland-2020-sessions.yaml')
