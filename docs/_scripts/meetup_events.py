import yaml
import glob
import io
import meetup.api

from pprint import pprint

def load_yaml(path):
    with io.open(path, encoding='utf-8') as fp:
        return yaml.safe_load(fp)

def load_meetups():
    result = []
    for yaml_file in glob.glob('../_data/meetups/*.yaml'):
        meetup = load_yaml(yaml_file)
        if not 'website' in meetup:
            raise SphinxError('Meetup needs a website')
        result.append(meetup['website'])
    return result


meetups = load_meetups()

client = meetup.api.Client()

for m in meetups:
    # Substring the meetup.com and trailing slash. EWWW
    #print(m[23:-1])

    t = client.GetEvents(group_urlname=m[23:-1])

    for e in t.results:
        pprint('##'+e['group']['name'])
        pprint(e['name'])
        pprint(e['event_url'])
        #
        #  'time': 1522803600000,
        #  'updated': 1521572914000,
        #  'utc_offset': -25200000,
        #
