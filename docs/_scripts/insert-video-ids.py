"""

1. Install yt-dlp
2. yt-dlp --print "%(id)s,%(title)s" https://www.youtube.com/playlist?list=PLZAeFn6dfHpneQPsDWa4OmEpgW4pNiaZ2  > docs/_scripts/playlist.txt
3. Edit `__main__` and run
4. Commit `_data/`  with new added video ids

"""

from pathlib import Path
from ruamel import yaml
import Levenshtein

import sys

docs_root = str(Path(__file__).resolve().parents[1])
sys.path.append(docs_root)

from _ext.utils import load_yaml


def add_yt_ids(speaker_yaml_file):
    talks = load_yaml(speaker_yaml_file)
    playlist_path = '_scripts/playlist.txt'
    playlist_data = load_yt_playlist(playlist_path)

    for index, talk in enumerate(talks):
        schedule_title = talk['title']
        yt_id = find_most_similar_title(playlist_data, schedule_title)
        talk['youtubeId'] = yt_id

    yaml.round_trip_dump(talks, open(speaker_yaml_file, 'w+'), default_flow_style=False)


def load_yt_playlist(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                yt_id, title = line.split(',', 1)
                data.append((yt_id, title))
    return data

def find_most_similar_title(playlist_data, query_title):
    max_similarity = 0
    most_similar_id = ''

    for yt_id, yt_title in playlist_data:
        similarity = Levenshtein.ratio(query_title.lower(), yt_title.lower())
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_id = yt_id

    return most_similar_id


if __name__ == '__main__':
    add_yt_ids('_data/portland-2024-sessions.yaml')
