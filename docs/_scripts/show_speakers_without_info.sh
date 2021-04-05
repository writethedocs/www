#!/bin/bash

# List speakers who have not completed all questions in Pretalx
# See pretalx2mc-info.py for details about the API authentication

python pretalx2mc-info.py
yq '.[].speakers[] | select(.pronouns == null) | .name' ../_data/mc-info.yaml