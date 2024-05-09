import asyncio
import requests
from bs4 import BeautifulSoup
import re
import yaml
import os
from datetime import datetime, timezone
from dateutil import tz
import json

# This script scrapes the pages for meetups to see if there are upcoming events.
# If there are, they're returned in the right format for the newsletter.

# To run it, install the necessary dependencies and run the script with Python
# such as `python docs/_scripts/get_upcoming_meetups.py`.
# Then copy the resulting list into the newsletter article.

# Look at a specific Meetup.com page and return data for any upcoming events
async def get_events_info(meetup_link):
    # Make a GET request to the Meetup organization page
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, f"{meetup_link['url']}?type=upcoming")

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all upcoming events
    upcoming_events = soup.find_all('a', id=re.compile('event-card'))
    # If there are no upcoming events, return an object with at least the location
    if not upcoming_events:
        return [{'date': None, 'url': None, 'title': None,'location': meetup_link['location']}]
    else:
        events_info = []
        # Loop through each event element
        for event in upcoming_events:
            # Get the URL for the event
            event_link = event.get('href')
            # Get the event page
            response = await asyncio.get_event_loop().run_in_executor(None, requests.get, event_link)

            # Parse the HTML content of the page using BeautifulSoup
            event_soup = BeautifulSoup(response.content, 'html.parser')
            
            # Get JSON object with info on the event
            event_data_raw = event_soup.find("script", {"id": "__NEXT_DATA__"})
            event_json = json.loads(event_data_raw.contents[0])
            event_data = event_json['props']['pageProps']['event']

            # Extract the date and timezone for the event
            dateTime = event_data['dateTime']
            event_timezone = event_data['timezone'] 

            # Get the event name
            event_title = event_soup.find('h1').getText()

            # Add all data on the event to the list
            events_info.append({'date': dateTime, 'timezone': event_timezone, 'url': event_link, 'title': event_title,'location': meetup_link['location']})
        return events_info

# Separate the link checks into asynchronous events and do them at once
async def check_urls(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_events_info(url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

# Load YAML files on meetups
yaml_directory = "docs/_data/meetups"
yaml_files = [f for f in os.listdir(yaml_directory) if f.endswith(".yaml")]

# Get the meetup locations and urls for each meetup YAML file
meetup_links = []
for yaml_file in yaml_files:
    with open(os.path.join(yaml_directory, yaml_file), "r") as f:
        data = yaml.safe_load(f)
        location = ""
        # If the city property exists
        try:
            # If city is explicitly blank, use the state
            if data['city'] == None:
                location = f"{data['state']}, {data['country']}"
            else:
                location = f"{data['city']}, {data['country']}"
        # If no city, just use the country
        except KeyError:
            location = f"{data['country']}"
        meetup_links.append({"location": location, "url": f"https://www.meetup.com/{data['meetup']}/events"})

# Run the URL checks asynchronously
results = asyncio.run(check_urls(meetup_links))

# Iterate over each result and add info on events within the defined number of days
days_within = 37
upcoming_events = []
for result in results:
    # Handle locations with no results
    if len(result) == 0:
        continue
    # Handle events with no date
    if result[0]['date'] == None:
        continue
    # Handle events with data
    for event in result:
        current_datetime = datetime.now(timezone.utc)
        event_date = current_datetime
        try:
            event_date = datetime.fromisoformat(event['date'])
        except:
            # If a problem with time zone, just ignore it
            event_date = datetime.strptime(event['date'].rsplit(' ',1)[0], '%a, %b %d, %Y, %I:%M %p')
        if (event_date - current_datetime).days <= days_within:
            event['date'] = event_date
            upcoming_events.append(event)

# Sort the links by date
sorted_upcoming_events = sorted(upcoming_events, key=lambda upcoming_event: upcoming_event['date'])

# Turn into newsletter format
upcoming_event_links = []
for upcoming_event in sorted_upcoming_events:
    upcoming_event_links.append(f"- {upcoming_event['date'].strftime('%-d %b, %H:%M')} {upcoming_event['date'].astimezone(tz=tz.gettz(upcoming_event['timezone'])).tzname()} ({upcoming_event['location']}): `{upcoming_event['title']} <{upcoming_event['url']}>`__")

print('\n'.join(upcoming_event_links))