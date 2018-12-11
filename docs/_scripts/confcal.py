from delorean import Delorean, parse
from datetime import timedelta, datetime
from ics import Calendar, Event
import sys
import argh
import io
import yaml

events = {
    'Announce conference & CFP': {'notice': 175, 'audience': 'Conf list'},
    'Instructions for CFP review': {'notice': 125, 'audience': 'Review panel'},
    'CFP reminder': {'notice': 123, 'audience': 'Conf list'},
    'CFP closes': {'notice': 120, 'audience': 'None'},
    'Send accept/reject emails': {'notice': 102, 'audience': 'CFP applicants'},
    'Finalize headshots, abstracts': {'notice': 92, 'audience': 'Speakers'},
    'Announce speakers': {'notice': 88, 'audience': 'Conf list'},
    'Call for volunteers': {'notice': 60, 'audience': 'Conf list'},
    'Promote events & activities': {'notice': 45, 'audience': 'Conf list'},
    'Confirm schedule with speakers': {'notice': 38, 'audience': 'Speakers'},
    'Announce full schedule': {'notice': 30, 'audience': 'Conf list'},
    'Speaker venue email': {'notice': 21, 'audience': 'Speakers'},
    'Volunteer email': {'notice': 7, 'audience': 'Volunteers'},
    'Final speaker email': {'notice': 7, 'audience': 'Speakers'},
    'Get ready': {'notice': 47, 'audience': 'Attendees'},
    'Welcome': {'notice': 3, 'audience': 'Attendees'},
    'Conference': {'notice': 0, 'audience': 'Attendees'},
    'Thanks': {'notice': -3, 'audience': 'Conf list'},
}

def load_yaml(path):
    with io.open(path, encoding='utf-8') as fp:
        return yaml.safe_load(fp)

def dates(date, events=events):
    "Takes the first day of the conf (dd/mm/yy)"
    "outputs dates to stdout, and writes dates to confdates.yaml"
    "Edit that file if you want to tweak the dates before creating the ICS"

    d = Delorean()
    d = parse(date, dayfirst=True)

    test = dict()
    for name, info in events.items():
        date=(d-timedelta(days=info['notice'])).format_datetime('dd MMMM yyyy', locale='en_GB')
        print(name, 'on', date )
        test.update({name:{'date': date, 'audience': info['audience']}})

    yaml.dump(test, open('confdates.yaml', 'w+'))

def ics():
    "Writes stored dates to ICS format."
    data = load_yaml('confdates.yaml')
    #yaml.dump(data,sys.stdout)

    cal = Calendar()

    for name, info in data.items():
        event = Event()
        event.name = name + ' [' + info['audience'] + ']'
        event.begin = parse(info['date']).datetime
        cal.events.add(event)

    with open('confdates.ics', 'w') as f:
       f.writelines(cal)

parser = argh.ArghParser()
parser.add_commands([dates, ics])

if __name__ == '__main__':
    parser.dispatch()
