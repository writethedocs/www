import yaml
import glob
import io
import meetup.api
import collections

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

##############################################################
meetups = load_meetups()

# if we want to test output for only the ATX & Berlin meetups:
# meetups = ["https://www.meetup.com/WriteTheDocs-ATX-Meetup/",
#     "https://www.meetup.com/Write-The-Docs-Berlin/"]

client = meetup.api.Client()
##############################################################

# get relevant data for meetups: name, time, url, venue

relevant_results = {}

for meetup in meetups:
    # Substring the meetup.com and trailing slash. EWWW
    #print(m[23:-1])

    t = client.GetEvents(group_urlname=meetup[23:-1])

    for event in t.results:

        # convert UTC time to human-readable dates
        # FIX: getting incorrect dates; possible time zone problem
        event_date = strftime("%B %d", gmtime(event['time']))
        event_name = event['name']
        event_url = event['event_url']

        if 'venue' in event:
            # city = event['venue']['city']
            # country = event['localized_country_name']
            # event_venue = city + ', ' + country
            event_venue = event['venue']['city']
        else:
            event_venue = event['group']['name'][15:]

        relevant_results[event_date] = {
            'name': event_name,
            'url': event_url,
            'venue': event_venue
        }

# FIX: sorting by alphabetical order, i.e., "April" -> "August"
ordered_results = collections.OrderedDict(sorted(relevant_results.items()))

pprint(ordered_results)

##################################################
# pprint('##'+event['group']['name'])
# pprint(event['name'])
# pprint(event['event_url'])

#  'time': 1522803600000,
#  'updated': 1521572914000,
#  'utc_offset': -25200000,

# TODO:
# x sort by time

# - filter out events later than 2 months from now