import csv
import os
import sys

import requests
from datetime import datetime
from bs4 import BeautifulSoup

# How to run:
# Update details below
# $ export HOPIN_LOGIN = 'email:password'
# $ python hopin_export_old.py <csv path>

HOPIN_USERNAME, HOPIN_PASSWORD = os.environ['HOPIN_LOGIN'].split(':', 1)
CSV_TIME_FORMAT = '%d %b %Y %I:%M %p'
HOPIN_TIME_FORMAT = '%Y-%m-%d+%H:%M'
HOPIN_TIMEZONE = 'Pacific+Time+(US+&+Canada)'
STAGE_ID = 33435  # id for the main stage
SCHEDULE_ID = 111638  # id for the whole schedule, not individual segments, extract from session add URL
HOPIN_URL = 'https://hopin.to/organisers/events/wtd-portland-2020'

# end of config

LOGIN_URL = 'https://hopin.to/users/sign_in'
session = requests.Session()


def login():
    payload = {
        'user[email]': HOPIN_USERNAME,
        'user[password]': HOPIN_PASSWORD,
        'commit': 'Sign+in',
        'authenticity_token': get_authenticity_token(LOGIN_URL)
    }
    r = session.post(LOGIN_URL, params=payload)
    if r.status_code != 200:
        print(f'Failed to log in: response {r.status_code}')
        print(r.text)
        exit(1)


def get_authenticity_token(url):
    r = session.get(url)
    if r.status_code != 200:
        print(f'Failed to retrieve token: response {r.status_code}')
        exit(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    token_tag = soup.find('input', attrs={'type': 'hidden'})
    return token_tag.get('value')


def get_segments():
    segments = {}
    r = session.get(HOPIN_URL + '/schedules')
    if r.status_code != 200:
        print(f'Failed to retrieve segments: response {r.status_code}')
        exit(1)
    soup = BeautifulSoup(r.text, 'html.parser')
    for tr in soup.find('tbody').find_all('tr'):
        row_id = tr['id'].replace('schedule-', '')
        name = tr.find_next('td').text.strip()
        segments[name] = row_id
    return segments


def create_segment(schedule_type, name, description, start, end):
    payload = {
        'event_part_type': schedule_type.lower(),
        'schedule[name]': name,
        'schedule[description]': description,
        'schedule[time_start]': start.strftime(HOPIN_TIME_FORMAT),
        'schedule[time_end]': end.strftime(HOPIN_TIME_FORMAT),
        'schedule[timezone]': HOPIN_TIMEZONE,
        #'schedule[speakers][]': '43762'
        'button': '',
    }
    if schedule_type.lower() == 'stage':
        payload['schedule[backstage_id]'] = STAGE_ID

    payload['authenticity_token'] = get_authenticity_token(HOPIN_URL + '/schedules/new')

    r = session.post(HOPIN_URL + '/schedules', params=payload)
    if r.status_code == 200:
        print(f'Created segment {name}')
    else:
        print(f'Failed to create segment {name}: response {r.status_code}')
        exit(1)


def create_session(name, description, priority, schedule_id=''):
    payload = {
        'roundtable[name]': name,
        'roundtable[description]': description,
        'roundtable[can_sit]': 'anyone_',
        'roundtable[can_watch]': 'anyone',
        'roundtable[max_participants]': '20',
        'roundtable[priority]': str(priority),
        'roundtable[schedule_id]': str(schedule_id),
        'roundtable[record_status]': '0',
        'roundtable[picture]': '',
        'button': '',
        'authenticity_token': get_authenticity_token(f'{HOPIN_URL}/schedule/{SCHEDULE_ID}/roundtables/new')
    }

    r = session.post(f'{HOPIN_URL}/schedule/{SCHEDULE_ID}/roundtables', params=payload)
    if r.status_code == 200:
        print(f'Created session {name}')
    else:
        print(f'Failed to create session {name}: response {r.status_code}')
        exit(1)


def main():
    login()

    csv_type = sys.argv[1]
    if csv_type not in ['sessions', 'schedule']:
        raise ValueError(f'Unknown CSV type: {csv_type}')
    with open(sys.argv[2]) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if csv_type == 'schedule':
                start_str, end_str, name, description, schedule_type = row[:5]
                start = datetime.strptime(start_str, CSV_TIME_FORMAT)
                end = datetime.strptime(end_str, CSV_TIME_FORMAT)
                create_segment(schedule_type, name, description, start, end)

            elif csv_type == 'sessions':
                name, description, priority = row[:3]
                create_session(name, description, priority)

main()
