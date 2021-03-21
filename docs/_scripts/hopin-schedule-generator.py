import csv
import re
from datetime import datetime, timedelta

from _ext.core import load_conference_context_from_yaml

HOPIN_STAGE_NAME = 'Stage'
DAYS = {
    'writing_day': '2020-10-18',
    'talks_day1': '2020-10-19',
    'talks_day2': '2020-10-20',
}
TIMEZONE = '+02:00'
HOPIN_TIME_FORMAT = '%Y-%m-%d %H:%M %z'
SHORTCODE = 'prague'
YEAR = '2020'

# This script might be a bit broken, needs re-evaluation before the next hopin import.

####################

data = load_conference_context_from_yaml(SHORTCODE, int(YEAR), YEAR, None)

with open('hopin-schedule.csv', 'w') as f:
    csvwriter = csv.writer(f)

    csvwriter.writerow(['Start time', 'End time', 'Schedule name', 'Schedule description', 'Segment name', 'Stage name', 'Tags'])
    for day, sessions in data['schedule'].items():
        for session in sessions:
            start = datetime.strptime(DAYS[day] + ' ' + session['time'] + ' ' + TIMEZONE, HOPIN_TIME_FORMAT)
            end = start
            description = ''
            if 'data' in session:
                end = start + timedelta(minutes=45)
                description = f'Main stage talk. Full description: https://www.writethedocs.org/conf/{SHORTCODE}/{YEAR}/speakers/#speaker-{session["data"]["speakers"][0]["slug"]}'
            if 'title' in session:
                match = re.search(r'(\d+) mins', session['title'])
                if match:
                    end = start + timedelta(minutes=int(match.group(1)))

            csvwriter.writerow([
                start.strftime(HOPIN_TIME_FORMAT),
                end.strftime(HOPIN_TIME_FORMAT),
                session['title'] if 'title' in session else session['data']['title'],
                description,
                'stage',
                HOPIN_STAGE_NAME,
            ])

