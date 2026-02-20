#!/usr/bin/bash

for branch in $(sed -n 's/- \(f.*\)/\1/p;s/- \(el.*\)/\1/p' .github/workflows/update-branch.yml | tr -d ' '); do

if [[ $branch == f* ]]; then
  export releasever=${branch/f/}
else
  export releasever=$branch
fi

# Begin check hell to not strain our servers or waste CI time if a key already exists
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever ] && curl -s https://repos.fyralabs.com/terra$releasever/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-source ] && curl -s https://repos.fyralabs.com/terra$releasever-source/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-source
if [[ $releasever != el* ]]; then
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-extras ] && curl -s https://repos.fyralabs.com/terra$releasever-extras/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-extras
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-extras-source ] && curl -s https://repos.fyralabs.com/terra$releasever-extras-source/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-extras-source
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-mesa ] && curl -s https://repos.fyralabs.com/terra$releasever-mesa/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-mesa
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-mesa-source ] && curl -s https://repos.fyralabs.com/terra$releasever-mesa-source/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-mesa-source
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-multimedia ] && curl -s https://repos.fyralabs.com/terra$releasever-multimedia/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-multimedia
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-multimedia-source ] && curl -s https://repos.fyralabs.com/terra$releasever-multimedia-source/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-multimedia-source
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-nvidia ] && curl -s https://repos.fyralabs.com/terra$releasever-nvidia/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-nvidia
[ ! -f anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-nvidia-source ] && curl -s https://repos.fyralabs.com/terra$releasever-nvidia-source/key.asc > anda/terra/gpg-keys/RPM-GPG-KEY-terra$releasever-nvidia-source
fi

done
