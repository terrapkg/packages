#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021-2024 Simone Caronni <negativo17@gmail.com>
# Licensed under the GNU General Public License Version or later

import json
import sys
import xml.etree.ElementTree as ElementTree

def main():
    if len(sys.argv) != 3:
        print("usage: %s supported-gpus.json com.nvidia.driver.metainfo.xml" % sys.argv[0])
        return 1

    json_input = open(sys.argv[1])
    gpus_raw = json.load(json_input)
    legacy = 'legacybranch'
    devids = []

    for product in gpus_raw["chips"]:

        if legacy not in product.keys():

            devid = int(product["devid"], 16)
            if not devid in devids:
                devids.append(devid)

    appstream_xml = ElementTree.parse(sys.argv[2])
    root = appstream_xml.getroot()
    provides = ElementTree.Element('provides')
    root.append(provides)

    for devid in devids:
        modalias = ElementTree.SubElement(provides, "modalias")
        modalias.text = "pci:v000010DEd%08Xsv*sd*bc*sc*i*" % (devid)

    ElementTree.indent(root, space="  ", level=0)
    # appstream-util validate requires the xml header
    appstream_xml.write(sys.argv[2], encoding="utf-8", xml_declaration=True)

if __name__ == "__main__":
    main()
