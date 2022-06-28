# Generate a CFP review sheet from Pretalx
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


def get_all_speakers(pretalx_slugs, output_file):
    if not os.environ.get('PRETALX_TOKEN'):
        print('Error: PRETALX_TOKEN not found in environment variables.')
        return
    http_headers = {'Authorization': 'Token ' + os.environ['PRETALX_TOKEN']}

    events_list = []
    for slug in pretalx_slugs:
        url = f'https://pretalx.com/api/events/{slug}'
        print(f'Loading event from {url}...')
        response = requests.get(url, headers=http_headers)
        if response.status_code != 200:
            print(f'Error: request failed: {response.status_code}: {response.text}')
            return
        events_list.append(response.json())

    submissions_list = []
    for event in events_list:
        submissions_url = f'https://pretalx.com/api/events/{event["slug"]}/submissions/'
        print(f'Loading submissions from {submissions_url}...')
        event_submissions = load_pretalx_resource(submissions_url, http_headers)
        for submission in event_submissions:
            submission['event'] = event['name']['en']
            submission['year'] = event['date_from'].split('-')[0]
        submissions_list += event_submissions

    with open(output_file, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["Speaker", "Talk", "Conference", "Year", "Status"])
        for submission in submissions_list:
            speakers = ', '.join([speaker['name'] for speaker in submission['speakers']])
            csvwriter.writerow([
                speakers,
                submission['title'],
                submission['event'].replace(submission['year'], '').strip(),
                submission['year'],
                submission['state'],
            ])
    print(f'Wrote {len(submissions_list)} submissions to {output_file}')


def get_review_scores(pretalx_slug, output_file):
    if not os.environ.get('PRETALX_TOKEN'):
        print('Error: PRETALX_TOKEN not found in environment variables.')
        return
    http_headers = {'Authorization': 'Token ' + os.environ['PRETALX_TOKEN']}

    submissions_url = f'https://pretalx.com/api/events/{pretalx_slug}/submissions/'
    print(f'Loading submissions from {submissions_url}...')
    submissions_list = load_pretalx_resource(submissions_url, http_headers)
    submissions = {submission['code']: submission for submission in submissions_list}

    reviews_url = f'https://pretalx.com/api/events/{pretalx_slug}/reviews'

    reviews = load_pretalx_resource(reviews_url, http_headers)
    for review in reviews:
        try:
            submissions[review['submission']].setdefault("scores", []).append(float(review['score']))
        except KeyError:
            print(f"WARNING: Ignoring review {review['id']} for unknown submission {review['submission']}")
        except TypeError:
            print(f"WARNING: Ignoring review {review['id']} for missing/invalid score {review['score']}")

    with open(output_file, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["Mean", "Median", "Pvar", "Title", "Speaker", "Tags", "URL"])
        for code, submission in submissions.items():
            speakers = ', '.join([speaker['name'] for speaker in submission['speakers']])
            url = f"https://pretalx.com/orga/event/{pretalx_slug}/submissions/{code}/reviews/"
            scores = submission.get('scores', [0])
            csvwriter.writerow([
                "%.1f" % statistics.mean(scores),
                "%.1f" % statistics.median(scores),
                "%.1f" % statistics.pvariance(scores),
                submission['title'],
                speakers,
                ', '.join(submission['tags']),
                url,
            ])
    print(f'Wrote {len(submissions)} submissions to {output_file}')


# Might be reusable in other pretalx interfaces
def load_pretalx_resource(url, http_headers):
    results = []
    while url:
        response = requests.get(url, headers=http_headers)
        if response.status_code != 200:
            print(f'Error: request failed: {response.status_code}: {response.text}')
            return

        results += response.json()['results']

        if response.json()['next']:
            url = response.json()['next']
        else:
            break
    return results


if __name__ == '__main__':
    # get_review_scores(
    #     pretalx_slug='wtd-portland-2022',
    #     output_file='wtd-portland-2022-reviews.csv',
    # )
    get_all_speakers(
        pretalx_slugs=[
            'wtd-portland-2020',
            'write-the-docs-portland-2021',
            'wtd-portland-2022',
            'wtd-prague-2020',
            'write-the-docs-prague-2021',
            'wtd-prague-2022',
            'write-the-docs-australia-2020',
            'wtd-australia-and-india-2021',
        ],
        output_file='wtd-speakers.csv',
    )
