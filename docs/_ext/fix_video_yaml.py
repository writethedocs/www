import os
from ruamel import yaml

from sys import stdout
from core import slugify, load_yaml, load_conference_data, generate_video_slug

def fix_the_yaml(year, series, slug, yaml_file):

    # 2015
    # Write the Docs EU
    # eu
    # '../_data/2015.eu.speakers.yaml'

    talks = load_yaml(yaml_file)

    for index, talk in enumerate(talks):
        #print index
        #print '['+ str(index) + ']' + generate_video_slug(talk)
        talks[index]['year'] = year
        talks[index]['series'] = series
        talks[index]['event'] = series + ' ' + year
        talks[index]['series_slug'] = slug
        talks[index]['path'] = 'conf/' + talk['series_slug']+'/'+talk['year']+'/'+ 'videos'+'/'+ generate_video_slug(talk)
        talks[index]['slug'] = generate_video_slug(talk)
        talks[index]['speakers'] =  {'details': '', 'name': talks[index]['name'], 'img_file': slugify(talks[index]['name'])+'.png', 'slug': slugify(talks[index]['name']), 'twitter': '', 'website':''}

    yaml.safe_dump(talks, open(yaml_file, 'w+'), default_flow_style = False)

if __name__ == '__main__':
    #fix_the_yaml('2015', 'Write the Docs EU', 'eu', '../_data/2015.eu.speakers.yaml')
    #fix_the_yaml('2016', 'Write the Docs EU', 'eu', '../_data/2016.eu.speakers.yaml')
    #fix_the_yaml('2015', 'Write the Docs NA', 'na', '../_data/2015.na.speakers.yaml')
    #fix_the_yaml('2016', 'Write the Docs NA', 'na', '../_data/2016.na.speakers.yaml')
    fix_the_yaml('2018', 'Write the Docs Prague', 'prague', '../_data/2018.prague.speakers.yaml')
