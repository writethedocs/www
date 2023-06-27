import asyncio
import requests
from bs4 import BeautifulSoup
import re
import yaml
import os
from datetime import datetime, timezone

# This script scrapes the pages for meetups to see if there are upcoming events.
# If there are, they're returned in the right format for the newsletter.

# To run it, install the necessary dependencies and run the script with Python
# such as `python docs/_scripts/get_upcoming_meetups.py`.
# Then copy the resulting list into the newsletter article.
# All the times will be in your local timezone,
# so you may want to convert them to the timezone local to each meeting.

# Look at a specific Meetup.com page and return data for any upcoming events
async def get_events_info(meetup_link):
    # Make a GET request to the Meetup organization page
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, meetup_link['url'])

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the upcoming events div
    upcoming_events = soup.find('div', class_=re.compile('eventsList-upcomingEvents'))
    # If it doesn't exist, return an object with at least the location
    if upcoming_events is None:
        return [{'date': None, 'url': None, 'title': None,'location': meetup_link['location']}]
    else:
        # Find all event elements within the upcoming events div
        events = upcoming_events.find_all('div', class_="chunk")
        events_info = []
        # Loop through each event element
        for event in events:
            # Extract the date, URL, and title of each event
            date = event.find('time').get('datetime')
            event_link = event.find('a', class_="eventCard--link")
            event_url = event_link.get('href')
            event_title = event_link.find('span').get_text()
            events_info.append({'date': date, 'url': event_url, 'title': event_title,'location': meetup_link['location']})
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
        meetup_links.append({"location": location, "url": f"https://www.meetup.com/{data['meetup']}"})

# Run the URL checks asynchronously
results = asyncio.run(check_urls(meetup_links))

# Iterate over each result and add info on events within the defined number of days
days_within = 37
upcoming_events = []
for result in results:
    if result[0]['date'] == None:
        continue
    for event in result:
        event_date = datetime.fromtimestamp(int(event['date']) / 1000)
        if (event_date - datetime.now()).days <= days_within:
            event['date'] = event_date
            upcoming_events.append(event)

# Sort the links by date
sorted_upcoming_events = sorted(upcoming_events, key=lambda upcoming_event: upcoming_event['date'])

# Turn into newsletter format
upcoming_event_links = []
for upcoming_event in sorted_upcoming_events:
    upcoming_event_links.append(f"- {upcoming_event['date'].strftime('%-d %b, %H:%M %Z')} {datetime.now(timezone.utc).astimezone().tzinfo} ({upcoming_event['location']}): `{upcoming_event['title']} <https://www.meetup.com{upcoming_event['url']}>`__")

print('\n'.join(upcoming_event_links))