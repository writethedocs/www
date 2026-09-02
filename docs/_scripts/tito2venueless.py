# This script does the following:
# - Find all completed attendees in tito
# - Filter for ones that have no current venueless link
# - Connect and auth to the venueless websockets API
# - For each ticket that has no venueless link yet:
#   - Determine traits based on ticket type
#   - Also set the tito ticket reference as a trait to allow permission finetuning later
#   - Get a login link from Venueless for these traits
#   - Save the link in tito
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
# Activity names not listed in here cause a warning. List them with an empty
# list of traits to acknowledge that they intentionally grant no traits.
ACTIVITY_NAME_TO_TRAIT = {
    "in-person conference": ["onsite"],
    "virtual conference": ["virtual"],
    "in-person paid tickets": [],
}
# If not listed in here, only gets DEFAULT_TRAITS
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
assert hello_response.json()["authenticated"]

pending_tickets = []

# NOTE: in tito UI, this is called an attendee.
# The expand parameter is only supported from API version 3.1, which is not the
# default. Without it, tito silently omits the activities from each ticket.
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
    if warning := tickets_page["meta"].get("warning"):
        print(f"Error: tito API warning: {warning}")
        sys.exit(1)
    tito_tickets += tickets_page["tickets"]
    page = tickets_page["meta"]["next_page"]

print(f"Found {len(tito_tickets)} tickets.")

for ticket in tito_tickets:
    ticket_slug = ticket["slug"]
    ticket_reference = ticket["reference"]
    venueless_meta = ticket.get("metadata").get("venueless") if ticket.get("metadata") else None

    # "release" is the API term for what the UI calls "ticket"
    release_title = ticket["release"]["title"]
    traits = TICKET_NAME_TO_TRAIT.get(release_title.lower(), []).copy()
    traits += DEFAULT_TRAITS
    traits.append(ticket_reference)

    activity_names = [activity["name"].lower() for activity in ticket.get("activities", [])]
    if not activity_names:
        print(f"NOTE: ticket {ticket_reference} has no activities, no onsite/virtual trait set")
    for activity_name in activity_names:
        if activity_name in ACTIVITY_NAME_TO_TRAIT:
            traits += ACTIVITY_NAME_TO_TRAIT[activity_name]
        else:
            print(f"NOTE: ticket {ticket_reference} has unknown activity {activity_name!r}, skipping it")

    # Tickets that are neither onsite nor virtual, e.g. workshop only, get no venueless access
    is_attending = "onsite" in traits or "virtual" in traits
    print(f'Found ticket {ticket["name"]}: {ticket_reference=} {traits=} {venueless_meta=} {is_attending=}')
    if not venueless_meta and is_attending:
        pending_tickets.append((ticket_slug, traits))

VENUELESS_WSS_URL = f"{VENUELESS_PUBLIC_URL.replace('https', 'wss')}ws/world/{VENUELESS_EVENT_SLUG}/"

with connect(VENUELESS_WSS_URL) as ws_client:
    venueless_rq_count = 1
    ws_client.send(json.dumps(["authenticate", {"token": VENUELESS_JWT}]))
    message = json.loads(ws_client.recv())
    assert message[1]["user.config"]

    for ticket_slug, traits in pending_tickets:
        ws_client.send(
            json.dumps(["world.tokens.generate", venueless_rq_count, {"number": 1, "days": 90, "traits": traits}])
        )
        message = json.loads(ws_client.recv())
        assert message[0] == "success"
        assert message[1] == venueless_rq_count
        token = message[2]["results"][0]
        venueless_url = f"{VENUELESS_PUBLIC_URL}login/{token}"
        venueless_rq_count += 1

        tickets_update_response = requests.patch(
            f"https://api.tito.io/v3/writethedocs/{TITO_EVENT}/tickets/{ticket_slug}",
            json={"metadata": json.dumps({"venueless": venueless_url})},
            headers=headers,
        )
        print(f"Updated venueless link for ticket {ticket_slug}: {venueless_url}")
