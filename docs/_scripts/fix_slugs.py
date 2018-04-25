from os.path import dirname, abspath
import sys

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import yaml
from _ext.core import slugify

yaml_files = ['_data/na-2018-day-1.yaml', '_data/na-2018-day-2.yaml']

for yaml_file in yaml_files:
    day1 = yaml.safe_load(open(yaml_file))
    for d in day1:
        if u'\u2013' in d['Session']:
            d['Slug'] = slugify(d['Session'].split(u'\u2013')[1])
    yaml.safe_dump(day1, open(yaml_file, 'w+'), default_flow_style=False)
