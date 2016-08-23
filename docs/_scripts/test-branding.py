#!/usr/bin/env python

import os
import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))


def searchthis(location, searchterm):
    invalid = False
    for dir_path, dirs, file_names in os.walk(location):
        for file_name in file_names:
            fullpath = os.path.join(dir_path, file_name)
            for line in file(fullpath):
                if searchterm in line:
                    print "[{file}:{num}] {line}".format(
                        file=file_name,
                        num='?',
                        line=line,
                    )
                    invalid = True
    return invalid

wrong_branding = searchthis(d, "Write " + "The Docs")

if wrong_branding:
    print "Branding is broken!"
    sys.exit(1)
else:
    print "Branding looks good!"
    sys.exit(0)
