#!/bin/bash
set -e

cd "$(dirname "$0")"

# Only lint configs for 2026 and newer. Older conferences are frozen, so we
# don't validate them and can require more fields on current configs.
for y in ../_data/*-config.yaml
do
    [[ $y == *"schema"* ]] && continue
    year=$(echo "$y" | grep -oE '[0-9]{4}')
    [[ -n $year && $year -lt 2026 ]] && continue
	yamale -s docs/_data/schema-config.yaml $y -p ruamel
done

# Note that this and the next check only covers 2020 and newer schedules
for y in ../_data/*-schedule.yaml
do
    [[ $y == *"schema"* ]] && continue
	yamale -s docs/_data/schema-schedule.yaml $y -p ruamel
done

for y in ../_data/*-sessions.yaml
do
    [[ $y == *"schema"* ]] && continue
	yamale -s docs/_data/schema-sessions.yaml $y -p ruamel
done

cd -
