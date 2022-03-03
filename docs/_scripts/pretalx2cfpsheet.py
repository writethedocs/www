# Generate a sessions YAML from Pretalx talk selections.
# To use:
# - Get an API token from https://pretalx.com/orga/me
# - Update the parameters at the end of this file, if needed (e.g. conference name)
# - Do: export PRETALX_TOKEN=<your token>
# - Go to directory docs/_scripts
# - Run this script
import shutil
import sys
sys.path.insert(1, '../_ext')

import os
from collections import OrderedDict
import requests

def get_review_scores(pretalx_slug):
    if not os.environ.get('PRETALX_TOKEN'):
        print('Error: PRETALX_TOKEN not found in environment variables.')
        return
    http_headers = {'Authorization': 'Token ' + os.environ['PRETALX_TOKEN']}

    submissions_url = f'https://pretalx.com/api/events/{pretalx_slug}/submissions/?state=submitted'
    print(f'Loading submissions from {submissions_url}...')

    while(submissions_url):
        submissions = requests.get(submissions_url, headers=http_headers)
        if submissions.status_code != 200:
            print(f'Error: submissions request failed: {submissions.status_code}: {submissions.text}')
            return

        for index, talk in enumerate(submissions.json()['results']):
            print(talk['code']+'    '+talk['title'])

        if submissions.json()['next']:
            submissions_url = submissions.json()['next']
        else:
            submissions_url=False

    reviews_url = f'https://pretalx.com/api/events/{pretalx_slug}/reviews'
    print(f'Loading reviews from {reviews_url}...')

    while(reviews_url):
        reviews = requests.get(reviews_url, headers=http_headers)
        if reviews.status_code != 200:
            print(f'Error: reviews request failed: {reviews.status_code}: {reviews.text}')
            return

        for index, review in enumerate(reviews.json()['results']):
            if isinstance(review['score'], str):
                print(review['submission']+'    '+review['score'])

        if reviews.json()['next']:
            reviews_url = reviews.json()['next']
        else:
            reviews_url=False

if __name__ == '__main__':
    get_review_scores(
        pretalx_slug='wtd-portland-2022'
    )
