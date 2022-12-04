import requests
import re
from datetime import datetime


NAME = 'prismlauncher-nightly'
REPO = "PrismLauncher/PrismLauncher"
REGEX_SHA = r'%global commit (.+)'
SPEC = f"{NAME}.spec"
LINK = f'https://api.github.com/repos/{REPO}/commits/HEAD'

sha = requests.get(LINK, headers={'Authorization': 'Bearer ' + os.getenv('GITHUB_TOKEN')}).json()['sha']
f = open(SPEC, 'r')

matches = re.findall(REGEX_SHA, txt:=f.read())
if not len(matches): exit(f"{NAME}: Failed to match regex!")
cur = matches[0]

if sha == cur: exit(f'{NAME}: Up to date!')
print(f'{NAME}: {cur} -> {sha}')

newspec = re.sub(REGEX_SHA, f'%global commit {sha}', txt)

f.close()
f = open(SPEC, 'w')
f.write(newspec)
f.close()
