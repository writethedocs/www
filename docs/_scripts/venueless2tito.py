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

TITO_EVENT = "write-the-docs-atlantic-2024"
VENUELESS_PUBLIC_URL = "https://writethedocs.venueless.events/"  # include trailing /
VENUELESS_EVENT_SLUG = "wtd24"
TICKET_NAME_TO_TRAIT = {
    "staff": ["staff"],
    "speaker": ["speaker"],
    "sponsor": ["sponsor"],
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

# NOTE: in tito UI, this is called an attendee
tickets_response = requests.get(
    f"https://api.tito.io/v3/writethedocs/{TITO_EVENT}/tickets",
    params={"page[size]": 1000, "search[states][]": "complete", "expand": "release"},
    headers=headers,
)
for ticket in tickets_response.json()["tickets"]:
    ticket_slug = ticket["slug"]
    ticket_reference = ticket["reference"]
    venueless_meta = ticket.get("metadata").get("venueless") if ticket.get("metadata") else None

    # "release" is the API term for what the UI calls "ticket"
    traits = TICKET_NAME_TO_TRAIT.get(ticket["release"]["title"].lower(), []).copy()
    traits += DEFAULT_TRAITS
    traits.append(ticket_reference)

    is_staff = ticket["release"]["title"] == "Staff"
    print(f'Found ticket {ticket["name"]}: {ticket_reference=} {traits=} {venueless_meta=} {is_staff=}')
    if not venueless_meta and is_staff:
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
