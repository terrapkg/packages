import requests
import re

NAME = 'prismlauncher'
REPO = "PrismLauncher/PrismLauncher"
REGEX_COMMIT = r"^%define commit (.+)$"
SPEC = f"{NAME}.spec"


obj = requests.get(f'https://api.github.com/repos/{REPO}/commits/develop').json()
commit = obj['sha']

f = open(SPEC, 'r')
match = re.match(REGEX_COMMIT, txt:=f.read(), re.RegexFlag.M)
if not match: exit(f"{NAME}: Failed to match regex!")
cur_commit = match.group(1)
if commit == cur_commit:
    exit(f'{NAME}: Up to date!')
print(f'{NAME}: {cur_commit} -> {commit}')
newspec = re.sub(REGEX_COMMIT, f'%define commit {commit}', txt, flags=re.RegexFlag.M)
f.close()
f = open(SPEC, 'w')
f.write(newspec)
f.close()
