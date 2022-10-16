import os
import re
from requests import get


def run_cmds(*cmds: str):
    for cmd in cmds:
        print(f"chkupdate: $ {cmd}")
        if rc := os.system(cmd):
            exit(f"chkupdate: Stopping because {rc=}")


SPEC = 'discord-canary.spec'
REGEX = r'Version:(\s+)([\.\d]+)\n'
LINK = 'https://discordapp.com/api/download/canary?platform=linux&format=tar.gz'

html = get(LINK, allow_redirects=False).text
newver = re.findall(r'https://dl-canary\.discordapp\.net/apps/linux/([\.\d]+)/', html)
if not any(newver):
    exit("chkupdate: Failed to parse html!")
newver = newver[0]

f = open(SPEC, 'r')
content = f.read()
found = re.findall(REGEX, content)
try:
    assert found
    curver = found[0][1]
    if newver == curver:
        print("chkupdate: Up to date!")
        exit()
    else:
        print(f"chkupdate: {curver} -> {newver}")
except IndexError or AssertionError:
    exit("chkupdate: Failed to read spec!")

newspec = re.sub(REGEX, f'Version:{found[0][0]}{newver}\n', content, 1)
f.close()
f = open(SPEC, 'w')
f.write(newspec)
f.close()

run_cmds(f"wget https://discordapp.com/api/download/canary?platform=linux&format=tar.gz")
