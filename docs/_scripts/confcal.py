from delorean import Delorean, parse
from datetime import timedelta, datetime
from ics import Calendar, Event

conf = "2019/05/19 00:00:00 -0800"

d = Delorean()
d = parse(conf)

events = {
  'Announce Conference & CFP': 175,
  'Instructions for CFP Review': 125,
  'CFP Reminder': 123,
  'CFP closes': 120,
  'Send Accept/Reject Emails': 102,
  'Finalize headshots, abstracts': 92,
  'Announce Speakers': 88,
  'Call for Volunteers': 60,
  'Promote Events & Activities': 45,
  'Confirm schedule with speakers': 38,
  'Announce schedule': 30,
  'Speaker venue email': 21,
  'Volunteer email': 7,
  'Final speaker email': 7,
  'Get ready': 47,
  'Welcome': 3,
  'Conference': 0,
  'Thanks': -3,
}

c = Calendar()

for key, value in events.items():
  #print(key, 'at conf minus', value, 'days', 'on', (d-timedelta(days=value)).format_datetime('dd MMMM yyyy', locale='en_GB'))

  e = Event()
  start = d-timedelta(days=value)
  e.name = key
  e.begin = start.datetime
  c.events.add(e)

with open('wtd.ics', 'w') as f:
   f.writelines(c)
