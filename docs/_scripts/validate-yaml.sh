#!/bin/bash
set -e

cd "$(dirname "$0")"

for y in ../_data/config-* ../_data/*-config.yaml
do
    [[ $y == *"schema"* ]] && continue
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
