#!/bin/bash

# List speakers who have not completed all questions in Pretalx
# See pretalx2mc-info.py for details about the API authentication

#python pretalx2mc-info.py

# {
#  "title": "Beyond metrics: Using maturity models to develop a docs strategy",
#  "speaker": "Sarah R. Rodlund",
#  "pronouns": "She, Her, Hers / They, Their, Theirs",
#  "facts": "At the moment, in no specific order, my favorite things are bicycles, the Pacific Ocean, hanging out with my elderly cat, Otis, learning Spanish, and of course, writing!.",
#  "pronounce": "Exactly like the English version here: https://translate.google.com/?hl=en&sl=en&tl=sv&text=Rod%20Lund&op=translate"
#}

yq -r '.[] | {title: .title, speaker: .speakers[].name, pronouns: .speakers[].pronouns, facts: .speakers[].facts, pronounce: .speakers[].pronounce} | "## "+.speaker + " ("+ .pronouns+")\n### "+ .title +"\n\n"+ .facts +"\n\nName pronunciation guide: "+ .pronounce +"\n"' ../_data/mc-info.yaml > mc-info.md