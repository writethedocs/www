#!/bin/bash

# List speakers who have not completed all questions in Pretalx
# See pretalx2mc-info.py for details about the API authentication

# Either uncomment the following line or run python pretalx2mc-info.py separately
#python pretalx2mc-info.py

yq -r '.[] | {title: .title, speaker: .speakers[].name, pronouns: .speakers[].pronouns, facts: .speakers[].facts, pronounce: .speakers[].pronounce} | "## "+.speaker + " ("+ .pronouns+")\n### "+ .title +"\n\n"+ .facts +"\n\nName pronunciation guide: "+ .pronounce +"\n"' ../_data/mc-info.yaml > mc-info.md