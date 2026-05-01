#!/bin/sh
# Ensure a docker-compose.local.yml exists for the devcontainer.
# Runs on the HOST before the container starts (initializeCommand).
#
# Priority:
#   1. Already exists in .devcontainer/ — do nothing
#   2. User has one at ~/.devcontainer/docker-compose.local.yml — symlink it
#   3. Otherwise — create a no-op stub

LOCAL=".devcontainer/docker-compose.local.yml"

if [ -e "$LOCAL" ]; then
    exit 0
fi

HOME_OVERRIDE="$HOME/.devcontainer/docker-compose.local.yml"
if [ -f "$HOME_OVERRIDE" ]; then
    ln -s "$HOME_OVERRIDE" "$LOCAL"
    exit 0
fi

echo 'services: {}' > "$LOCAL"
