import yaml
import glob
import io
import meetup.api
import collections

from time import strftime, gmtime, time, localtime
from datetime import datetime

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

# Expects $MEETUP_API_KEY to de defined as an environment variable

meetups = load_meetups()
client = meetup.api.Client()

# get relevant data for meetups: name, time, url, venue

relevant_results = {}

for meetup in meetups:
    # Substring the meetup.com and trailing slash. EWWW
    #print(m[23:-1])

    t = client.GetEvents(group_urlname=meetup[23:-1])

    for event in t.results:

        event_date= event['time']/1000.0
        # convert UTC time to human-readable dates
        human_date = strftime("%B %d", localtime(event_date))

        if 'venue' in event:
            # Country seems not to work? Unsure why? FIXME
            # city = event['venue']['city']
            # country = event['localized_country_name']
            # event_venue = city + ', ' + country
            event_venue = event['venue']['city']
        else:
            event_venue = event['group']['name'][15:]

        relevant_results[event_date] = {
            'name': event['name'],
            'human_date': human_date,
            'event_date': event_date,
            'url': event['event_url'],
            'venue': event_venue,
        }

# Newsletter format!
# - 6 May - Denver, CO, USA - `WTD and STC Dine-Around <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/261045278/>`__

for event in sorted(relevant_results):
    #print(event, relevant_results[event])
    print('- ' + relevant_results[event]['human_date'] + ' - ' + relevant_results[event]['venue']  + ' - `' +  \
                 relevant_results[event]['name'] + ' <' + relevant_results[event]['url'] + '>`__')

# TODO output an RST page with a cron job for the website
