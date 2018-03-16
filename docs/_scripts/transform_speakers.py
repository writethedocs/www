"""
Uses a speakers.json Google contacts export run through jsoncsv::

    cat speakers.csv |csvjson -i 4 > speakers.json

Then the 2016.json is Lanyrd data.
"""
from __future__ import print_function
import json

data = json.load(open('2016.json'))
speaker_data = json.load(open('speakers.json'))

speakers = {}

for s in speaker_data:
    try:
        firstname = s['Name'].split(' ')[0].lower()
        speakers[firstname] = s['E-mail 1 - Value']
    except:
        print("FAIL")

print(speakers)

for day in data['sessions']:
    for talk in day['sessions']:
        talk['release'] = True
        for speaker in talk['speakers']:
            firstname = speaker['name'].split(' ')[0].lower()
            try:
                speaker['email'] = speakers[firstname]
                talk['email'] = speakers[firstname]
            except:
                print("FAIL")
                print(firstname)
