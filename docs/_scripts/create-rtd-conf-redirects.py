#!/usr/bin/env python3
"""
Create Read the Docs redirects for the 2013-2017 conference URLs.

Those conferences were published under /conf/na/, /conf/eu/ and /conf/au/.
From 2018 on we use city names, so people guess /conf/portland/2016/ and get
a 404. This maps the city-style URLs onto the ones that exist.

Redirects live in the Read the Docs project, not in this repository, so this
script is the version-controlled record of what should be configured. It is
idempotent: existing redirects with the same source are left alone.

This project is served without a version prefix (writethedocs.org/conf/...,
not /en/latest/conf/...), so these are `page` redirects, whose source paths
carry no language or version prefix.

Requires:
    - RTD_TOKEN environment variable (Read the Docs API token, from
      https://app.readthedocs.org/accounts/tokens/)
    - requests package

Usage:
    python docs/_scripts/create-rtd-conf-redirects.py --dry-run
    RTD_TOKEN=<token> python docs/_scripts/create-rtd-conf-redirects.py
"""

import argparse
import os
import sys
import time

import requests

RTD_PROJECT = "writethedocs-www"
RTD_API_URL = f"https://app.readthedocs.org/api/v3/projects/{RTD_PROJECT}/redirects/"

# City name used from 2018 onwards -> the path segment the old site published
# under, and the years that exist for it.
CONFERENCES = [
    ("portland", "na", ["2015", "2016", "2017"]),
    ("prague", "eu", ["2015", "2016", "2017"]),
    ("australia", "au", ["2017"]),
]


def collect_redirects():
    """
    Build the redirect list.

    Each conference gets two rules. The wildcard covers the sub-pages, and the
    bare conference home gets its own rule rather than relying on the wildcard
    to match an empty suffix.
    """
    redirects = []
    for city, old, years in CONFERENCES:
        for year in years:
            redirects.append(
                {
                    "from_url": f"/conf/{city}/{year}/",
                    "to_url": f"/conf/{old}/{year}/",
                    "description": f"{city.title()} {year} was published under /conf/{old}/",
                }
            )
            redirects.append(
                {
                    "from_url": f"/conf/{city}/{year}/*",
                    "to_url": f"/conf/{old}/{year}/:splat",
                    "description": f"{city.title()} {year} sub-pages",
                }
            )
    return redirects


def existing_sources(token):
    """Return the from_url of every redirect already on the project."""
    sources = set()
    url = RTD_API_URL
    while url:
        resp = requests.get(url, headers={"Authorization": f"Token {token}"})
        resp.raise_for_status()
        payload = resp.json()
        for redirect in payload.get("results", []):
            sources.add(redirect.get("from_url"))
        url = payload.get("next")
    return sources


def create_redirect(token, redirect):
    resp = requests.post(
        RTD_API_URL,
        headers={"Authorization": f"Token {token}"},
        json={
            "type": "page",
            "from_url": redirect["from_url"],
            "to_url": redirect["to_url"],
            "description": redirect["description"],
            # These URL schemes are not coming back.
            "http_status": 301,
        },
    )
    if resp.status_code == 201:
        return True
    if resp.status_code == 429:
        retry_after = int(resp.headers.get("Retry-After", 60))
        print(f"  rate limited, waiting {retry_after}s...")
        time.sleep(retry_after)
        return create_redirect(token, redirect)
    print(f"  FAILED ({resp.status_code}) {redirect['from_url']}: {resp.text[:200]}")
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument(
        "--dry-run", action="store_true", help="Show what would be created"
    )
    args = parser.parse_args()

    redirects = collect_redirects()

    if args.dry_run:
        for redirect in redirects:
            print(f"  {redirect['from_url']} -> {redirect['to_url']}")
        print(f"\n{len(redirects)} redirects would be created")
        return 0

    token = os.environ.get("RTD_TOKEN")
    if not token:
        print("Error: RTD_TOKEN environment variable is required", file=sys.stderr)
        return 1

    already = existing_sources(token)
    created = skipped = failed = 0
    for redirect in redirects:
        if redirect["from_url"] in already:
            print(f"  exists, skipping: {redirect['from_url']}")
            skipped += 1
            continue
        if create_redirect(token, redirect):
            print(f"  created: {redirect['from_url']} -> {redirect['to_url']}")
            created += 1
        else:
            failed += 1
        time.sleep(0.5)

    print(f"\nCreated {created}, skipped {skipped}, failed {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
