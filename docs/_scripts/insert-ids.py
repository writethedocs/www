"""

1. Install yt-dlp
2. yt-dlp --print "%(id)s,%(title)s" https://www.youtube.com/playlist?list=PLZAeFn6dfHpneQPsDWa4OmEpgW4pNiaZ2  > docs/_scripts/playlist.txt
3. Edit `__main__` and run
4. Commit `_data/`  with new added video ids

"""

from pathlib import Path
from ruamel import yaml
from pprint import pprint
import Levenshtein

import sys

docs_root = str(Path(__file__).resolve().parents[1])
sys.path.append(docs_root)

from _ext.utils import load_yaml

def insert_id(yaml_file):

    file_path = '_scripts/playlist.txt' 
    loaded_data = load_data(file_path)
    talks = load_yaml(yaml_file)

    for index, talk in enumerate(talks):
        existing_string = talk['title']
        yt_id = find_most_similar_title(loaded_data, existing_string)
        talk['youtubeId'] = yt_id

    yaml.round_trip_dump(talks, open(yaml_file, 'w+'), default_flow_style=False)


def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                id_, title = line.split(',', 1)
                data.append((id_, title))
    return data

def find_most_similar_title(loaded_data, query_title):
    max_similarity = 0
    most_similar_title = None

    for id_, title in loaded_data:
        similarity = Levenshtein.ratio(query_title.lower(), title.lower())
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_title = title

    return id_

if __name__ == '__main__':
    insert_id('_data/portland-2023-sessions.yaml')
