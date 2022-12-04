import os
import re
from requests import get
import json

NAME = "authy"
SPEC = f"{NAME}.spec"
REGEX_VER = r'Version:(\s*)([\.\d]+)\n'
REGEX_SRC = r'Source0:(\s*)([^\n]+)\n'

def run_cmds(*cmds: str):
    for cmd in cmds:
        print(f"{NAME}: $ {cmd}")
        if rc := os.system(cmd):
            exit(f"{NAME}: Stopping because {rc=}")

raw = get('https://api.snapcraft.io/v2/snaps/info/authy', headers={'Snap-Device-Series': '16'}).text
data = json.loads(raw)
ver = data['channel-map'][0]['version']
f = open(SPEC, 'r')
content = f.read()
found = re.findall(REGEX_VER, content)
try:
    assert found
    curver = found[0][1]
    if ver == curver:
        exit(f"{NAME}: Up to date!")
    print(f"{NAME}: {curver} -> {ver}")
except IndexError or AssertionError:
    exit(f"{NAME}: Failed to read spec!")

link = data['channel-map'][0]['download']['url']
newspec = re.sub(REGEX_VER, f'Version:{found[0][0]}{ver}\n', content)
newspec = re.sub(REGEX_SRC, f'Source0:{found[0][0]}{link}\n', newspec)
f.close()
f = open(SPEC, 'w')
f.write(newspec)
f.close()
