import os
import re
from requests import get


NAME = 'discord-canary'
SPEC = f'{NAME}.spec'
REGEX = r'Version:(\s+)([\.\d]+)\n'
REGEX_LINK = r'https://dl-canary\.discordapp\.net/apps/linux/([\.\d]+)/'
LINK = 'https://discordapp.com/api/download/canary?platform=linux&format=tar.gz'


def run_cmds(*cmds: str):
    for cmd in cmds:
        print(f"{NAME}: $ {cmd}")
        if rc := os.system(cmd):
            exit(f"{NAME}: Stopping because {rc=}")

html = get(LINK, allow_redirects=False).text
newver = re.findall(REGEX_LINK, html)
if not any(newver):
    exit(f"{NAME}: Failed to parse html!")
newver = newver[0]

f = open(SPEC, 'r')
content = f.read()
found = re.findall(REGEX, content)
try:
    assert found
    curver = found[0][1]
    if newver == curver:
        exit(f"{NAME}: Up to date!")
    else:
        print(f"{NAME}: {curver} -> {newver}")
except IndexError or AssertionError:
    exit(f"{NAME}: Failed to read spec!")

run_cmds(f'rpmdev-bumpspec -n {newver} {SPEC}')
