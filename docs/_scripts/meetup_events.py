import yaml
import glob
import io
import meetup.api
import json

from time import strftime, gmtime

from pprint import pprint

def load_yaml(path):
    with io.open(path, encoding='utf-8') as filepath:
        return yaml.safe_load(filepath)

def load_meetups():
    meetup_urls = []
    for yaml_file in glob.glob('../_data/meetups/*.yaml'):
        meetup = load_yaml(yaml_file)
        if not 'website' in meetup:
            raise SphinxError('Meetup needs a website')
        meetup_urls.append(meetup['website'])
    return meetup_urls


meetups = load_meetups()

# if we want to test output for only the ATX & Berlin meetups:
# meetups = ["https://www.meetup.com/WriteTheDocs-ATX-Meetup/",
    # "https://www.meetup.com/Write-The-Docs-Berlin/"]

client = meetup.api.Client()

relevant_results = []

for meetup in meetups:
    # Substring the meetup.com and trailing slash. EWWW
    #print(m[23:-1])

    t = client.GetEvents(group_urlname=meetup[23:-1])

    for event in t.results:
        event_name = event['name']
        event_time = event['time']
        event_url = event['event_url']

        if 'venue' in event:
            event_venue = event['venue']['city']
        else:
            event_venue = event['group']['name'][15:]

        event_id = event_name + ' - ' + event_venue + ' - ' + str(event_time)

        event_json = json.JSONEncoder().encode(
            {
                event_id:
                    {
                        'name': event_name,
                        'time': event_time,
                        'url': event_url,
                        'venue': event_venue
                    }
            })

        relevant_results.append(event_json)

pprint(relevant_results)

        ##################################################
        # pprint('##'+event['group']['name'])
        # pprint(event['name'])
        # pprint(event['event_url'])

        ##################################################
        # ms_since_the_epoch = event['time']
        # date = strftime("%B %d", gmtime(event['time']))

        # if 'venue' in event:
        #     venue = event['venue']
        #     pprint(date + ' - ' + venue['city'])
        # else:
        #     venue = event['group']['name']
        #     pprint(date + ' - ' + venue)
        ##################################################

        #
        #  'time': 1522803600000,
        #  'updated': 1521572914000,
        #  'utc_offset': -25200000,
        #

# TODO:
# - sort by time
# - filter out events later than 2 months from now