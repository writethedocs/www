# This script does the following:
# - Find all completed attendees in tito, with their ticket type and activities
# - Filter for ones that attend onsite or virtually and have no current venueless link
# - Connect and auth to the venueless websockets API
# - For each of those tickets:
#   - Determine traits based on ticket type and activities
#   - Also set the tito ticket reference as a trait to allow permission finetuning later
#   - Get a login link from Venueless for these traits
#   - Save the link and its traits in tito
# - Warn about tickets whose traits changed since their link was made
#
# To use:
# - Set VENUELESS_JWT env to your venueless JWT token (get from `curl -D - your-login-URL`, or browser)
# - Set TITO_TOKEN to your tito token from https://id.tito.io/api-access-tokens
# - Update the settings block below to match your event


import json
import os
from pathlib import Path

import sys

import requests
from websockets.sync.client import connect

docs_root = str(Path(__file__).resolve().parents[1])
sys.path.append(docs_root)

###############################################################################
# Settings

TITO_EVENT = "write-the-docs-berlin-2026"
VENUELESS_PUBLIC_URL = "https://writethedocs.venueless.events/"  # include trailing /
# Pull this from the websocket path in a browser
VENUELESS_EVENT_SLUG = "wtdberlin26"
# Activity names differ per event, check them in the tito UI. Unlisted names abort the
# run, so list one with no traits to record that it intentionally grants none.
ACTIVITY_NAME_TO_TRAIT = {
    "in-person conference": ["onsite"],
    "virtual conference": ["virtual"],
    "in-person paid tickets": [],
}
# Ticket types that get more than DEFAULT_TRAITS. Names that match no ticket are reported.
TICKET_NAME_TO_TRAIT = {
    "staff ticket": ["staff"],
    "speaker ticket": ["speaker"],
    "volunteer ticket": ["volunteer"],
    "sponsor ticket": ["sponsor"],
}
DEFAULT_TRAITS = ["attendee"]

###############################################################################

assert VENUELESS_PUBLIC_URL[-1] == "/"

TITO_TOKEN = os.environ.get("TITO_TOKEN")
if not TITO_TOKEN:
    print("Error: TITO_TOKEN not found in environment variables.")
    sys.exit(1)

VENUELESS_JWT = os.environ.get("VENUELESS_JWT")
if not VENUELESS_JWT:
    print("Error: VENUELESS_JWT not found in environment variables.")
    sys.exit(1)

headers = {"Authorization": f"Token token={TITO_TOKEN}", "Accept": "application/json"}

hello_response = requests.get("https://api.tito.io/v3/hello", headers=headers)
assert hello_response.json()["authenticated"], hello_response.text

pending_tickets = []

# NOTE: in tito UI, a ticket is called an attendee.
# The expand parameter only works from API version 3.1, and tokens default to 3.0, where
# it is ignored and tickets come back without activities. 3.1 also returns leaner tickets,
# which is why the ticket type is read from the expanded release below.
tito_tickets = []
page = 1
while page:
    tickets_response = requests.get(
        f"https://api.tito.io/v3/writethedocs/{TITO_EVENT}/tickets",
        params={
            "version": "3.1",
            "page[number]": page,
            "page[size]": 100,
            "search[states][]": "complete",
            "expand": "release,activities",
        },
        headers=headers,
    )
    tickets_page = tickets_response.json()
    if "tickets" not in tickets_page:
        print(f"Error: unexpected tito response {tickets_response.status_code}: {tickets_response.text}")
        sys.exit(1)
    # Tito reports ignored parameters here rather than failing the request
    if warning := tickets_page["meta"].get("warning"):
        print(f"Error: tito API warning: {warning}")
        sys.exit(1)
    tito_tickets += tickets_page["tickets"]
    page = tickets_page["meta"]["next_page"]

print(f"Found {len(tito_tickets)} tickets.")

# Names that no longer match would quietly give everyone affected the wrong permissions,
# so check them before generating any tokens
activity_names = {activity["name"].lower() for ticket in tito_tickets for activity in ticket["activities"]}
if unknown_activities := activity_names - set(ACTIVITY_NAME_TO_TRAIT):
    print(f"Error: activities missing from ACTIVITY_NAME_TO_TRAIT: {sorted(unknown_activities)}")
    sys.exit(1)

# Only a note, because comped tickets stay incomplete until the recipient fills them in
release_titles = {ticket["release"]["title"].lower() for ticket in tito_tickets}
if unmatched_tickets := set(TICKET_NAME_TO_TRAIT) - release_titles:
    print(f"NOTE: no completed tickets for {sorted(unmatched_tickets)}, check they were not renamed in tito")
# A new privileged ticket type that nobody added to the settings shows up here
print(f"Ticket types without special roles: {sorted(release_titles - set(TICKET_NAME_TO_TRAIT))}")

for ticket in tito_tickets:
    ticket_reference = ticket["reference"]
    metadata = ticket["metadata"] or {}
    venueless_meta = metadata.get("venueless")

    # "release" is the API term for what the UI calls "ticket"
    traits = TICKET_NAME_TO_TRAIT.get(ticket["release"]["title"].lower(), []).copy()
    traits += DEFAULT_TRAITS
    traits.append(ticket_reference)
    for activity in ticket["activities"]:
        traits += ACTIVITY_NAME_TO_TRAIT[activity["name"].lower()]

    # Tickets that are neither onsite nor virtual, e.g. workshop only, get no venueless access
    is_attending = "onsite" in traits or "virtual" in traits
    if not is_attending:
        print(f"NOTE: ticket {ticket_reference} is neither onsite nor virtual, so gets no venueless link")
    print(f'Found ticket {ticket["name"]}: {ticket_reference=} {traits=} {venueless_meta=} {is_attending=}')
    if not venueless_meta and is_attending:
        pending_tickets.append((ticket, traits))
    # Traits can change after a link was made, e.g. when someone switches to onsite. Links
    # made before we started storing traits have none, so there is nothing to compare there.
    if (link_traits := metadata.get("venueless_traits")) and sorted(link_traits) != sorted(traits):
        print(f"WARNING: link for {ticket_reference} has {sorted(link_traits)}, needs {sorted(traits)}")

VENUELESS_WSS_URL = f"{VENUELESS_PUBLIC_URL.replace('https', 'wss')}ws/world/{VENUELESS_EVENT_SLUG}/"

with connect(VENUELESS_WSS_URL) as ws_client:
    venueless_rq_count = 1
    ws_client.send(json.dumps(["authenticate", {"token": VENUELESS_JWT}]))
    message = json.loads(ws_client.recv())
    assert message[1]["user.config"], message

    for ticket, traits in pending_tickets:
        ticket_slug = ticket["slug"]
        ticket_reference = ticket["reference"]
        ws_client.send(
            json.dumps(["world.tokens.generate", venueless_rq_count, {"number": 1, "days": 90, "traits": traits}])
        )
        message = json.loads(ws_client.recv())
        assert message[0] == "success", message
        assert message[1] == venueless_rq_count, message
        token = message[2]["results"][0]
        venueless_url = f"{VENUELESS_PUBLIC_URL}login/{token}"
        venueless_rq_count += 1

        # Tito replaces the whole metadata object, so keep any keys we did not set. The traits
        # are stored to spot later changes, and to see what a link grants without decoding it.
        metadata = {**(ticket["metadata"] or {}), "venueless": venueless_url, "venueless_traits": traits}
        tickets_update_response = requests.patch(
            f"https://api.tito.io/v3/writethedocs/{TITO_EVENT}/tickets/{ticket_slug}",
            json={"metadata": json.dumps(metadata)},
            headers=headers,
        )
        if not tickets_update_response.ok:
            # The token exists now, so not saving it here leaves it valid but unreachable
            print(f"Error: could not save the link for ticket {ticket_reference}: {tickets_update_response.text}")
            print(f"Set this link on the ticket by hand: {venueless_url}")
            sys.exit(1)
        print(f"Updated venueless link for ticket {ticket_reference}: {venueless_url}")
