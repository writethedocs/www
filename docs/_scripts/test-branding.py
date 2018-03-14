#!/usr/bin/env python

from __future__ import print_function
import os
import sys
from os.path import dirname, abspath

parent_dir = dirname(dirname(abspath(__file__)))
eu_conf_dir = os.path.join(parent_dir, 'conf', 'eu')
na_conf_dir = os.path.join(parent_dir, 'conf', 'na')


def searchthis(location, searchterm):
    invalid = False
    for dir_path, dirs, file_names in os.walk(location):
        for file_name in file_names:
            fullpath = os.path.join(dir_path, file_name)
            for line in file(fullpath):
                if searchterm in line:
                    print("[{file}:{num}] {line}".format(
                        file=fullpath,
                        num='?',
                        line=line,
                    ))
                    invalid = True
    return invalid


wrong_branding = searchthis(parent_dir, "Write " + "The Docs")
eu_wrong_branding_1 = searchthis(eu_conf_dir, 'na-2016')
eu_wrong_branding_2 = searchthis(eu_conf_dir, '2016/na')
na_wrong_branding_1 = searchthis(na_conf_dir, 'eu-2016')
na_wrong_branding_2 = searchthis(na_conf_dir, '2016/eu')

if any([
    wrong_branding,
    eu_wrong_branding_1,
    eu_wrong_branding_2,
    na_wrong_branding_1,
    na_wrong_branding_2,
]):
    print("Branding is broken!")
    sys.exit(1)
else:
    print("Branding looks good!")
    sys.exit(0)
