import json

workshops = []
unconfs = []
talks = []

data = json.load(file('2017-na-speakers.json'))

for talk in data:
    if 'Workshop' in talk['title']:
        workshops.append(talk)
    elif 'Unconference' in talk['title']:
        unconfs.append(talk)
    else:
        talks.append(talk)

json.dump(workshops, open('2017/na-workshops.json', 'w+'), indent=4)
json.dump(unconfs, open('2017/na-unconfs.json', 'w+'), indent=4)
json.dump(talks, open('2017/na-talks.json', 'w+'), indent=4)
