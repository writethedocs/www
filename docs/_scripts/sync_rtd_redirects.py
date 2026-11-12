#!/usr/bin/env python3
"""Sync the redirects in docs/_data/redirects.yaml to Read the Docs.

Each entry in the YAML file is a site path (`from`) and where it now goes
(`to`, a site path or a full URL). The script lists the project's existing
redirects and creates an exact redirect for each entry that isn't there yet,
so running it again is safe. It never deletes anything: remove a redirect
in the Read the Docs dashboard if an entry comes out of the file.

The site is a single-version project, so paths are used as they are, with
no /en/latest prefix. Redirects are created as 301s, since the pages are
gone for good.

Requires:
    - RTD_TOKEN environment variable (Read the Docs API token)
    - PyYAML and requests packages (both in the project's dependencies)

Usage:
    RTD_TOKEN=<token> uv run docs/_scripts/sync_rtd_redirects.py
    uv run docs/_scripts/sync_rtd_redirects.py --dry-run
"""

import argparse
import os
import sys
import time
from pathlib import Path

import requests
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
REDIRECTS_FILE = REPO_ROOT / "docs" / "_data" / "redirects.yaml"

RTD_PROJECT = "writethedocs-www"
RTD_API_URL = f"https://readthedocs.org/api/v3/projects/{RTD_PROJECT}/redirects/"


def load_redirects() -> list[tuple[str, str]]:
    with REDIRECTS_FILE.open(encoding="utf-8") as fp:
        entries = yaml.safe_load(fp) or []
    redirects = []
    for entry in entries:
        from_url, to_url = entry["from"], entry["to"]
        if not from_url.startswith("/"):
            sys.exit(f"'from' must be a site path starting with /: {from_url}")
        redirects.append((from_url, to_url))
    return redirects


def existing_redirects(session: requests.Session) -> dict[str, str]:
    """Map from_url to to_url for the redirects already on Read the Docs."""
    found = {}
    url = RTD_API_URL + "?limit=100"
    while url:
        resp = session.get(url)
        resp.raise_for_status()
        data = resp.json()
        for redirect in data["results"]:
            found[redirect["from_url"]] = redirect["to_url"]
        url = data.get("next")
    return found


def create_redirect(session: requests.Session, from_url: str, to_url: str) -> bool:
    resp = session.post(
        RTD_API_URL,
        json={"type": "exact", "from_url": from_url, "to_url": to_url, "http_status": 301},
    )
    if resp.status_code == 201:
        return True
    if resp.status_code == 429:
        retry_after = int(resp.headers.get("Retry-After", 60))
        print(f"  Rate limited, waiting {retry_after}s...")
        time.sleep(retry_after)
        return create_redirect(session, from_url, to_url)
    print(f"  FAILED ({resp.status_code}): {from_url} -> {resp.text[:200]}")
    return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync redirects.yaml to Read the Docs")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created")
    args = parser.parse_args()

    redirects = load_redirects()
    print(f"{len(redirects)} redirects in {REDIRECTS_FILE.relative_to(REPO_ROOT)}")

    token = os.environ.get("RTD_TOKEN")
    if not token:
        if args.dry_run:
            for from_url, to_url in redirects:
                print(f"  {from_url} -> {to_url}")
            print("\nSet RTD_TOKEN to compare against the redirects on Read the Docs.")
            return 0
        print("Error: RTD_TOKEN environment variable is required", file=sys.stderr)
        return 1

    session = requests.Session()
    session.headers["Authorization"] = f"Token {token}"
    existing = existing_redirects(session)
    print(f"{len(existing)} redirects on Read the Docs")

    created = failed = 0
    for from_url, to_url in redirects:
        if from_url in existing:
            state = "ok" if existing[from_url] == to_url else f"differs: -> {existing[from_url]}"
            print(f"  exists ({state}): {from_url}")
            continue
        if args.dry_run:
            print(f"  would create: {from_url} -> {to_url}")
            continue
        if create_redirect(session, from_url, to_url):
            print(f"  created: {from_url} -> {to_url}")
            created += 1
        else:
            failed += 1
        time.sleep(0.5)

    if not args.dry_run:
        print(f"\nCreated {created} redirects, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
