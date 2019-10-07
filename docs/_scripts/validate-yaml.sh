#!/bin/bash
set -e

cd "$(dirname "$0")"

for y in ../_data/config-* ../_data/*-config.yaml
do
    [[ $y == *"schema"* ]] && continue
	yamale --strict -s docs/_data/schema-config.yaml $y -p ruamel
done

cd -
