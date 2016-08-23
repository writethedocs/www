#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
DOCSDIR="$(dirname "$DIR")"
echo "Checking doc path: $DOCSDIR"
! grep -R 'Write The Docs' $DOCSDIR
