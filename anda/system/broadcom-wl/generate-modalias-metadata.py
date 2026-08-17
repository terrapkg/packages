#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Richard Hughes <richard@hughsie.com>
# Licensed under the GNU General Public License Version or later
#
# Modified to parse broadcom-wl README_6.30.223.271.txt and for python3
# Copyright (C) 2018 Nicolas Viéville <nicolas.vieville@univ-valenciennes.fr>
# Usage example: 
#   python3 generate-modalias-metadata.py README_6.30.223.271.txt "SUPPORTED DEVICES" | \
#   xargs appstream-util add-provide com.broadcom.driver.wireless.hybrid.test.metainfo.xml

from __future__ import print_function
import sys

def main():
    if len(sys.argv) != 3:
        print("usage: %s README_FILE.txt \"header to match\"" % sys.argv[0])
        return 1

    # open file
    f = open(sys.argv[1])
    in_section = False
    in_table = False
    pids = []
    for line in f.readlines():

        # find the right data table
        if line.find(sys.argv[2]) != -1:
            in_section = True
            continue
        if not in_section:
            continue

        # remove Windows and Linux line endings
        line = line.replace('\r', '')
        line = line.replace('\n', '')

        # end of table
        if len(line) > 0 and not line.startswith('          '):
            in_table = False
            continue

        # empty line
        if len(line) == 0:
            continue

        # skip the header
        if line.startswith('          -----'):
            in_table = True
            continue
        if not in_table:
            continue

        # end of section
        if len(line) > 0 and not line.startswith('          '):
            in_section = False
            in_table = False
            continue

        if line.find('0x14e4') != -1:
            # get name
            pid = int((line.split("0x14e4",1)[1]).split()[0], 16)
            if not pid in pids:
                pids.append(pid)

    # output
    vid = 0x14e4
    print("pci:v%08xd*sv*sd*bc02sc80i*" % (vid))
    for pid in pids:
        print("pci:v%08xd%08xsv*sd*bc02sc80i*" % (vid, pid))

if __name__ == "__main__":
    main()
