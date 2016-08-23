#!/usr/bin/env bash
SCRIPT=$(readlink -f $0)
SCRIPTPATH=`dirname $SCRIPT`
! grep -R 'Write The Docs' $SCRIPTPATH
