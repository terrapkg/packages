import os
import re
from requests import get
import json

SPEC = "authy.spec"
REGEX_VER = r'Version:(\s*)([\.\d]+)\n'
REGEX_SRC = r'Source0:(\s*)([^\n]+)\n'

def run_cmds(*cmds: str):
    for cmd in cmds:
        print(f"chkupdate: $ {cmd}")
        if rc := os.system(cmd):
            exit(f"chkupdate: Stopping because {rc=}")

raw = get('https://api.snapcraft.io/v2/snaps/info/authy', headers={'Snap-Device-Series': '16'}).text
data = json.loads(raw)
ver = data['channel-map'][0]['version']

f = open(SPEC, 'r')
content = f.read()
found = re.findall(REGEX, content)
try:
    assert found
    curver = found[0][1]
    if ver == curver:
        exit("chkupdate: Up to date!")
    print(f"chkupdate: {curver} -> {ver}")
except IndexError or AssertionError:
    exit("chkupdate: Failed to read spec!")

link = data['channel-map'][0]['download']['url']
newspec = re.sub(REGEX_VER, f'Version:{found[0][0]}{ver}\n', ver)
newspec = re.sub(REGEX_SRC, f'Source0:{found[0][0]}{link}\n', link)
f.close()
f = open(SPEC, 'w')
f.write(newspec)
f.close()
