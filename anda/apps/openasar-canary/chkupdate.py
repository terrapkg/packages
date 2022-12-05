import requests
import re
import os


NAME = "openasar-canary"
REPO = "GooseMod/OpenAsar"
REGEX_SHA = r"%define commit (.+)"
SPEC = f"{NAME}.spec"
LINK = f"https://api.github.com/repos/{REPO}/commits/HEAD"

token = os.getenv("GITHUB_TOKEN")
sha = requests.get(LINK, headers={"Authorization": f"Bearer {token}"}).json()["sha"]
f = open(SPEC, "r")

matches = re.findall(REGEX_SHA, txt := f.read())
if not len(matches):
    exit(f"{NAME}: Failed to match regex!")
cur = matches[0]

if sha == cur:
    exit(f"{NAME}: Up to date!")
print(f"{NAME}: {cur} -> {sha}")
