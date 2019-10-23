"""
This script creates the correct link slug from the spreadsheet
timetable export by seeing if there is a - and getting the
name and title from it if there is (magic)

For example
"Responsive Content - Presenting Your information On Any Device \u2013 Mike Hamilton"
-> #mike-hamilton
"""

from os.path import dirname, abspath
import sys

d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

import yaml
from _ext.utils import slugify

yaml_files = ['_data/prague-2019-day-1.yaml', '_data/prague-2019-day-2.yaml']

for yaml_file in yaml_files:
    day1 = yaml.safe_load(open(yaml_file))
    for d in day1:
        if u'-' in d['Session']:
            d['Slug'] = slugify(
                d['Session'].split(u'-')[0].split('&')[0]
            )
    yaml.safe_dump(day1, open(yaml_file, 'w+'), default_flow_style=False)
