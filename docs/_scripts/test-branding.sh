#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DOCSDIR="$(dirname "$DIR")"
echo "Checking doc path: $DOCSDIR"
grep -R 'Write The Docs' $DOCSDIR

if [ $? -eq 0 ]
# Bash exits "0" when a line is detected.
# We need to invert this because detecting lines means an error.
then
  echo "Errors detected!"
  exit 1
else
  echo "Branding looks good"
fi
