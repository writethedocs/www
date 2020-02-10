import sys
sys.path.insert(1, '../_ext')

from collections import OrderedDict
from utils import slugify
import json
from ruamel import yaml
from ruamel.yaml.representer import RoundTripRepresenter
import markdown

yamldoc = []
# Prevent OrderedDict from being presented as YAML OMAP - we just want a regular YAML dict.
yaml.add_representer(OrderedDict, RoundTripRepresenter.represent_dict, representer=RoundTripRepresenter)

def convert_to_yaml(year, series, slug, pretalx_results, yaml_file):
    with open(pretalx_results) as json_file:
        talks = json.load(json_file)
        for index, talk in enumerate(talks['results']):
            yamldoc.append(OrderedDict([
                ('title', talk['title']),
                ('slug',slugify(talk['title'] + '-' + talk['speakers'][0]['name'])),
                ('series', series),
                ('series_slug', slug),
                ('year', int(year)),
                ('speakers', []),
                ('abstract', markdown.markdown(talk['abstract'])),

            ]))
            for s in talk['speakers']:
                yamldoc[index]['speakers'].append(OrderedDict([
                    ('name', s['name']),
                    ('slug', slugify(s['name'])),
                    ('avatar', s['avatar']),
                ]))

        yaml_obj=yaml.YAML(typ='safe')
        yaml_obj.Representer = RoundTripRepresenter
        yaml_obj.default_flow_style = False
        yaml_obj.dump(yamldoc, open(yaml_file, 'w+'))



if __name__ == '__main__':
    convert_to_yaml('2020', 'Write the Docs Portland', 'portland', 'talks.json', '../_data/portland-2020-sessions.yaml')
