import io
import re

import yaml


def slugify(slug):
    """
    Create a URL-appropriate slug of a string.
    Installed as a Jinja filter.
    """
    slug = slug.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def generate_video_slug(session):
    """
    Generate a slug for the video of a session, based on title/speakers.
    """
    if 'title' not in session:
        return u''
    title = session['title']
    for speaker in session.get('speakers', []):
        title += '-{}'.format(speaker.get('slug', speaker['name']))
    return slugify(title)


def normalize_session(session):
    """
    Ensure a dict representing a conference session contains
    a correct slug and youtube ID.
    """
    youtube_pattern = re.compile(r'https://www.youtube.com/watch\?v=(.+)')

    session['slug'] = generate_video_slug(session)
    if 'video' in session and 'youtube.com' in session['video']:
        mo = youtube_pattern.match(session['video'])
        if mo:
            session['youtubeId'] = mo.group(1)


def load_yaml(path):
    with io.open(path, encoding='utf-8') as fp:
        return yaml.safe_load(fp)
