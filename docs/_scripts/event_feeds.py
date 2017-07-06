import yaml
import feedparser
import glob
import io
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
        result.append(meetup['website']+'events/rss')
    return result

# Function to fetch the rss feed and return the parsed RSS
def parseRSS( rss_url ):
    return feedparser.parse( rss_url )

# Function grabs the rss feed headlines (titles) and returns them as a list
def getHeadlines( rss_url ):
    headlines = []

    feed = parseRSS( rss_url )
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines

# A list to hold all headlines
allheadlines = []

# List of RSS feeds that we will fetch and combine
newsurls = load_meetups()

#pprint(newsurls)

# Iterate over the feed urls
for url in newsurls:
    # Call getHeadlines() and combine the returned headlines with allheadlines
    allheadlines.extend( getHeadlines( url ) )

# Iterate over the allheadlines list and print each headline
for hl in allheadlines:
    print(hl)
