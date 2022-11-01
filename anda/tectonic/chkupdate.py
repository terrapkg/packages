import os
import requests
import re

NAME = 'tectonic'
REPO = "tectonic-typesetting/tectonic"
REGEX_VER = r'Version:\s*([\.\d]+)\n'
SPEC = f"{NAME}.spec"
LINK = f'https://api.github.com/repos/{REPO}/releases/latest'


ver = requests.get(LINK).json()['tag_name']
with open(SPEC, 'r') as f:
    matches = re.findall(REGEX_VER, f.read())
if not len(matches): exit(f"{NAME}: Failed to match regex!")
cur = matches[0]
if ver == cur: exit(f'{NAME}: Up to date!')
print(f'{NAME}: {cur} -> {ver}')
os.system(f'rpmdev-bumpspec -n {ver} {SPEC}')
