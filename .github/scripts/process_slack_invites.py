"""Notify a Slack moderator channel about new Slack-invite form submissions.

Reads a published Google Sheet (CSV) of form responses, finds rows newer than
the last run, and posts each one to a Slack incoming webhook so a moderator
can manually send the invite. State is tracked in a JSON file committed back
to the repo by the workflow.

Why this design: Slack shared-invite links expire (and have a use cap), and
the legacy ``users.admin.invite`` endpoint needs an unofficial admin token.
A webhook ping to a private moderator channel is the most boring, durable
option for a static site with no backend.

Required environment variables:
    SHEET_CSV_URL      Public CSV URL from "File > Share > Publish to web"
                       on the responses sheet linked to the Google Form.
    SLACK_WEBHOOK_URL  Incoming webhook for the moderator channel.

Optional:
    TIMESTAMP_COLUMN   Name of the timestamp column (default: "Timestamp").
    EMAIL_COLUMN       Name of the email column (default: auto-detect).
    NAME_COLUMN        Name of the name column (default: auto-detect).
"""

from __future__ import annotations

import csv
import io
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

STATE_PATH = Path(".github/slack-invites/state.json")
DEFAULT_TIMESTAMP_COLUMN = "Timestamp"


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"last_processed_timestamp": ""}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")


def fetch_rows(csv_url: str) -> list[dict]:
    with urllib.request.urlopen(csv_url, timeout=30) as resp:
        text = resp.read().decode("utf-8-sig")
    return list(csv.DictReader(io.StringIO(text)))


def pick_column(row: dict, explicit: str | None, candidates: list[str]) -> str | None:
    if explicit and explicit in row:
        return explicit
    for key in row:
        if key.strip().lower() in candidates:
            return key
    return None


def post_to_slack(webhook_url: str, payload: dict) -> None:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        if resp.status >= 300:
            raise RuntimeError(f"Slack webhook returned HTTP {resp.status}")


def format_message(row: dict, name_col: str | None, email_col: str | None) -> dict:
    name = (row.get(name_col) if name_col else None) or "(no name)"
    email = (row.get(email_col) if email_col else None) or "(no email)"
    extras = [
        f"*{key}:* {value}"
        for key, value in row.items()
        if key not in {name_col, email_col, DEFAULT_TIMESTAMP_COLUMN} and value
    ]
    lines = [
        ":wave: New Slack invite request",
        f"*Name:* {name}",
        f"*Email:* {email}",
    ]
    lines.extend(extras)
    return {"text": "\n".join(lines)}


def main() -> int:
    csv_url = os.environ["SHEET_CSV_URL"]
    webhook_url = os.environ["SLACK_WEBHOOK_URL"]
    timestamp_col = os.environ.get("TIMESTAMP_COLUMN", DEFAULT_TIMESTAMP_COLUMN)
    name_override = os.environ.get("NAME_COLUMN") or None
    email_override = os.environ.get("EMAIL_COLUMN") or None

    rows = fetch_rows(csv_url)
    if not rows:
        print("Sheet is empty.")
        return 0

    name_col = pick_column(rows[0], name_override, ["name", "full name", "your name"])
    email_col = pick_column(
        rows[0], email_override, ["email", "email address", "your email"]
    )

    state = load_state()
    last_ts = state.get("last_processed_timestamp", "")

    new_rows = [r for r in rows if (r.get(timestamp_col) or "") > last_ts]
    if not new_rows:
        print("No new submissions.")
        return 0

    new_rows.sort(key=lambda r: r.get(timestamp_col) or "")
    print(f"Found {len(new_rows)} new submission(s).")

    for row in new_rows:
        payload = format_message(row, name_col, email_col)
        try:
            post_to_slack(webhook_url, payload)
        except (urllib.error.URLError, RuntimeError) as exc:
            print(f"Failed to notify Slack for row {row}: {exc}", file=sys.stderr)
            return 1
        print(f"Notified: {row.get(email_col) if email_col else row}")

    state["last_processed_timestamp"] = new_rows[-1].get(timestamp_col) or last_ts
    save_state(state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
