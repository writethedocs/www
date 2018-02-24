import os
import yaml

from core import slugify, load_yaml, load_conference_data, generate_video_slug

def main():

    talks = load_yaml('../_data/2015.eu.speakers.yaml')

    for index, talk in enumerate(talks):
        #print index
        print generate_video_slug(talk)
        talks[index]['year'] = '2015'
        talks[index]['event'] = 'Write the Docs EU 2015'
        talks[index]['series'] = 'Write the Docs EU'
        talks[index]['series_slug'] = 'eu'
        talks[index]['path'] = 'conf/' + talk['series_slug']+'/'+talk['year']+'/'+ 'videos'+'/'+ generate_video_slug(talk)
        talks[index]['slug'] = generate_video_slug(talk)

    yaml.safe_dump(talks, open('test.yaml', 'w+'), default_flow_style=False)

if __name__ == '__main__':
    main()
