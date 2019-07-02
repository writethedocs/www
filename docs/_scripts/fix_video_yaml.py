from _ext.core import load_yaml
from _ext.utils import generate_video_slug
from ruamel import yaml


def fix_the_yaml(year, series, slug, yaml_file):
    """
    This script was written by Sam to fix missing
    items in the speaker YAML, used for generating videos
    """

    talks = load_yaml(yaml_file)

    for index, talk in enumerate(talks):
        # print index
        # print '['+ str(index) + ']' + generate_video_slug(talk)
        talks[index]['year'] = year
        talks[index]['series'] = series
        talks[index]['event'] = series + ' ' + year
        talks[index]['series_slug'] = slug
        talks[index]['path'] = 'conf/' + '/'.join([talk['series_slug'], talk['year'], 'videos', generate_video_slug(talk)])
        talks[index]['slug'] = generate_video_slug(talk)
        # talks[index]['speakers'] =  {'details': '', 'name': talks[index]['name'], 'img_file': slugify(talks[index]['name'])+'.png', 'slug': slugify(talks[index]['name']), 'twitter': '', 'website':''}

    yaml.safe_dump(talks, open(yaml_file, 'w+'), default_flow_style=False)


if __name__ == '__main__':
    fix_the_yaml('2018', 'Write the Docs Australia', 'australia', '../_data/2018.australia.speakers.yaml')
Ik
