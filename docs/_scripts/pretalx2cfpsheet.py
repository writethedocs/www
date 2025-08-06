# Generate a CFP review meeting sheet from Pretalx
# The resulting sheet is intended as an aid during the meeting,
# not as an ongoing data source.
#
# To use:
# - Get an API token from https://pretalx.com/orga/me
# - Update the parameters at the end of this file, if needed (e.g. conference name)
# - Do: export PRETALX_TOKEN=<your token>
# - Go to directory docs/_scripts
# - Run this script
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "_ext"))

import csv
import requests
import statistics


def get_review_scores(pretalx_slug, previous_slugs):
    output_file = pretalx_slug + '-cfp-reviews.csv'
    if not os.environ.get('PRETALX_TOKEN'):
        print('Error: PRETALX_TOKEN not found in environment variables.')
        return
    http_headers = {'Authorization': 'Token ' + os.environ['PRETALX_TOKEN']}

    submissions_url = f'https://pretalx.com/api/events/{pretalx_slug}/submissions/'
    print(f'Loading current submissions from {submissions_url}...')
    submissions_list = load_pretalx_resource(submissions_url, http_headers)
    submissions = {
        submission['code']: submission
        for submission in submissions_list
        if submission['state'] not in ['withdrawn', 'canceled']
    }

    previous_submissions = get_previous_submissions(previous_slugs, http_headers)

    reviews_url = f'https://pretalx.com/api/events/{pretalx_slug}/reviews'
    reviews = load_pretalx_resource(reviews_url, http_headers)
    speaker_names = get_speaker_names(pretalx_slug, http_headers)
    submission_types = get_submission_types(pretalx_slug, http_headers)
    tags = get_tags(pretalx_slug, http_headers)

    for review in reviews:
        try:
            submissions[review['submission']].setdefault("scores", []).append(float(review['score']))
        except KeyError:
            print(f"WARNING: Ignoring review {review['id']} for unknown submission {review['submission']}")
        except TypeError:
            print(f"WARNING: Ignoring review {review['id']} for missing/invalid score {review['score']}")

    with open(output_file, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["Mean", "Median", "Pvar", "Type", "Title", "Speaker", "Tags", "Previous submissions", "URL"])
        for code, submission in submissions.items():
            previous_for_speaker = {}
            for speaker_slug in submission['speakers']:
                previous_for_speaker.update(previous_submissions.get(speaker_slug, {}))
            previous_for_speaker_str = '; '.join([
                f'{state.title()}: {", ".join(sorted(events))}'
                for state, events in
                sorted(previous_for_speaker.items())
            ])
            url = f"https://pretalx.com/orga/event/{pretalx_slug}/submissions/{code}/reviews/"
            scores = submission.get('scores', [])
            speakers = ', '.join(speaker_names[speaker] for speaker in submission['speakers'])
            csvwriter.writerow([
                "%.1f" % statistics.mean(scores) if scores else '-',
                "%.1f" % statistics.median(scores) if scores else '-',
                "%.1f" % statistics.pvariance(scores) if scores else '-',
                submission_types[submission['submission_type']][0],
                submission['title'],
                speakers,
                ', '.join([tags[t] for t in submission['tags']]),
                previous_for_speaker_str,
                url,
            ])
    print(f'Wrote {len(submissions)} submissions to {output_file}')


def get_previous_submissions(pretalx_slugs, http_headers):
    events_list = []
    for slug in pretalx_slugs:
        url = f'https://pretalx.com/api/events/{slug}'
        print(f'Loading previous event from {url}...')
        response = requests.get(url, headers=http_headers)
        if response.status_code != 200:
            print(f'Error: request failed: {response.status_code}: {response.text}')
            return
        events_list.append(response.json())

    speakers_submissions = {}
    for event in events_list:
        submissions_url = f'https://pretalx.com/api/events/{event["slug"]}/submissions/'
        print(f'Loading previous submissions from {submissions_url}...')
        event_submissions = load_pretalx_resource(submissions_url, http_headers)
        for submission in event_submissions:
            for speaker in submission['speakers']:
                event_name = event['name']['en'].replace('Write the Docs', '').strip()
                state = submission['state']
                speakers_submissions.setdefault(speaker, {}).setdefault(state, set()).add(event_name)

    return speakers_submissions


def get_speaker_names(pretalx_slug, http_headers):
    url = f'https://pretalx.com/api/events/{pretalx_slug}/speakers/'
    print(f'Loading speaker names from {url}...')
    speaker_info = load_pretalx_resource(url, http_headers)
    return {
        s['code']: s['name'] for s in speaker_info
    }

def get_submission_types(pretalx_slug, http_headers):
    url = f'https://pretalx.com/api/events/{pretalx_slug}/submission-types/'
    print(f'Loading submission types names from {url}...')
    submission_types = load_pretalx_resource(url, http_headers)
    return {
        s['id']: s['name']['en'] for s in submission_types
    }

def get_tags(pretalx_slug, http_headers):
    url = f'https://pretalx.com/api/events/{pretalx_slug}/tags/'
    print(f'Loading tag names from {url}...')
    tags = load_pretalx_resource(url, http_headers)
    return {
        s['id']: s['tag'] for s in tags
    }

def load_pretalx_resource(url, http_headers):
    results = []
    while url:
        response = requests.get(url, headers=http_headers)
        # 403 may occur as a pretalx bug
        if response.status_code not in [200, 403]:
            print(f'Error: request failed: {response.status_code}: {response.text}')
            return

        results += response.json()['results']

        if response.json()['next']:
            url = response.json()['next']
        else:
            break
    return results


if __name__ == '__main__':
    get_review_scores(
        pretalx_slug='wtd-berlin-2025',
        previous_slugs=[
            'wtd-portland-2020',
            'wtd-prague-2020',
            'write-the-docs-australia-2020',
            'write-the-docs-portland-2021',
            'write-the-docs-prague-2021',
            'wtd-australia-and-india-2021',
            'wtd-prague-2022',
            'wtd-portland-2022',
            'wtd-atlantic-2023',
            'wtd-portland-2023',
            'wtd-australia-2023',
            'wtd-portland-2024',
            'wtd-atlantic-2024',
            'wtd-australia-2024',
            'wtd-portland-2025',
        ],
    )
