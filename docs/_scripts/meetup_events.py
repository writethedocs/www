import yaml
import glob
import io
import meetup.api

from time import strftime, gmtime

from pprint import pprint

def load_yaml(path):
    with io.open(path, encoding='utf-8') as filepath:
        return yaml.safe_load(filepath)

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

for meetup in meetups:
    # Substring the meetup.com and trailing slash. EWWW
    #print(m[23:-1])

    t = client.GetEvents(group_urlname=meetup[23:-1])

    for event in t.results:
        # pprint('##'+event['group']['name'])
        # pprint(event['name'])
        # pprint(event['event_url'])

        ##################################################
        ms_since_the_epoch = event['time']
        month = strftime("%B", gmtime(ms_since_the_epoch))
        day = strftime("%d", gmtime(ms_since_the_epoch))
        date = month + ' ' + day

        if 'venue' in event:
            venue = event['venue']
            pprint(date + ' - ' + venue['city'])
        else:
            pprint("LOOOOOOOOOK!!!!!!!")

            # this prints "March 10 - Australi" ... why???
            venue = event['group']['name'][15:-1]
            pprint(date + ' - ' + venue)
        ##################################################

        #
        #  'time': 1522803600000,
        #  'updated': 1521572914000,
        #  'utc_offset': -25200000,
        #

# we haven't passed any date restrictions in our request to the Meetup API,
# yet it only returns events that are (more or less) within 1 year from today
# (seems like no date restrictions) ... hm ...