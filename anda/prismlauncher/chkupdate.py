import requests
import re

REPO = "PrismLauncher/PrismLauncher"
REGEX_COMMIT = r"^%define commit (.+)$"


obj = requests.get(f'https://api.github.com/repos/{REPO}/commits/develop').json()
commit = obj['sha']
