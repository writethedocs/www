#!/bin/bash

# Print the slugs from the sessions so you can paste them into the schedule

yq '.[].slug' _data/portland-2021-sessions.yaml | tr -d '"'


