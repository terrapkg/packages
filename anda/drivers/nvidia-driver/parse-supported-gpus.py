#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Simone Caronni <negativo17@gmail.com>
# Licensed under the GNU General Public License Version or later

import json
import sys

def main():
    if len(sys.argv) != 2:
        print("usage: %s supported-gpus.json" % sys.argv[0])
        return 1

    f = open(sys.argv[1])
    gpus_raw = json.load(f)
    legacy = 'legacybranch'
    devids = []

    for product in gpus_raw["chips"]:

        if legacy not in product.keys():

            devid = int(product["devid"], 16)
            if not devid in devids:
                devids.append(devid)

    for devid in devids:
        print("pci:v000010DEd%08Xsv*sd*bc*sc*i*" % (devid))

if __name__ == "__main__":
    main()
