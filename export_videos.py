#!/usr/bin/env python3
"""Export all YouTube video titles, IDs, and slugs from session/speaker YAML files."""

import csv
import glob
import io
import os
import re
import sys
import yaml


def slugify(slug):
    slug = slug.encode('utf-8', 'ignore').lower().decode('utf-8')
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    slug = re.sub(r'[-]+', '-', slug)
    return slug


def generate_video_slug(session):
    if 'slug' in session:
        return session['slug']
    if 'title' not in session:
        return ''
    title = session['title']
    for speaker in session.get('speakers', []):
        title += '-{}'.format(speaker.get('slug', speaker['name']))
    return slugify(title)


def normalize_session(session):
    youtube_pattern = re.compile(r'https://www.youtube.com/watch\?v=(.+)')
    session['slug'] = generate_video_slug(session)
    if 'video' in session and 'youtube.com' in session.get('video', ''):
        mo = youtube_pattern.match(session['video'])
        if mo:
            session['youtubeId'] = mo.group(1)


def main():
    os.chdir(os.path.join(os.path.dirname(__file__), 'docs'))

    speakers_file_pattern = re.compile(r'(\d{4})\.(\w+)\.speakers')
    sessions_file_pattern = re.compile(r'(\w+)-(\d{4})-sessions')

    videos = []

    for f in sorted(glob.glob('_data/*.yaml')):
        base = os.path.splitext(os.path.basename(f))[0]

        mo = speakers_file_pattern.match(base)
        if mo:
            year = int(mo.group(1))
            region = mo.group(2)
            sessions = yaml.safe_load(io.open(f, encoding='utf-8'))
            if not sessions:
                continue
            for session in sessions:
                normalize_session(session)
                youtube_id = session.get('youtubeId', '')
                if youtube_id:
                    videos.append({
                        'title': session.get('title', ''),
                        'youtubeId': youtube_id,
                        'slug': session.get('slug', ''),
                        'year': year,
                        'region': region,
                        'speakers': ', '.join(s.get('name', '') for s in session.get('speakers', [])),
                    })
            continue

        mo = sessions_file_pattern.match(base)
        if mo:
            region = mo.group(1)
            year = int(mo.group(2))
            sessions = yaml.safe_load(io.open(f, encoding='utf-8'))
            if not sessions:
                continue
            for session in sessions:
                normalize_session(session)
                youtube_id = session.get('youtubeId', '')
                if youtube_id:
                    videos.append({
                        'title': session.get('title', ''),
                        'youtubeId': youtube_id,
                        'slug': session.get('slug', ''),
                        'year': year,
                        'region': region,
                        'speakers': ', '.join(s.get('name', '') for s in session.get('speakers', [])),
                    })

    # Sort by year, region, title
    videos.sort(key=lambda v: (v['year'], v['region'], v['title']))

    # Write CSV
    output_path = os.path.join(os.path.dirname(__file__), 'youtube_videos.csv')
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['title', 'youtubeId', 'slug', 'year', 'region', 'speakers'])
        writer.writeheader()
        writer.writerows(videos)

    print(f"Exported {len(videos)} videos to youtube_videos.csv")


if __name__ == '__main__':
    main()
