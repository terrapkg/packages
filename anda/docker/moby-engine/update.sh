#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2022 Maxwell G (@gotmax23)
# SPDX-License-Identifier: MIT

# USAGE: After bumping the version in moby-engine.spec and downloading the new
# sources, run this script in moby-engine's distgit repository to update the
# package's virtual Provides.

set -euo pipefail

# Note(gotmax23): I have a separate update.sh script in my $PATH.
# When that exists, this script will run that first.
# You can ignore this.
if command -v update.sh && [ "$#" -gt 0 ]; then
    update.sh "$@"
fi

spectool -g moby-engine.spec --define "_sourcedir ."
fedpkg prep

version="$(rpmspec -D '_sourcedir %(pwd)' -q --srpm --qf '%{version}\n' *.spec)"

cat << EOF > provides.spec.inc
# Bundled dependencies
Provides:       bundled(tini-static)
Provides:       bundled(golang(github.com/docker/docker))
Provides:       bundled(golang(github.com/docker/cli))
# grep -v -e '^$' -e '^#' cli-${version}/vendor/github.com/docker/distribution/vendor.conf | sort | awk '{print "Provides:       bundled(golang("\$1")) = "\$2}'
EOF

grep -v -e '^$' -e '^#' "moby-${version}/cli-${version}/vendor/github.com/docker/distribution/vendor.conf" | sort | awk '{print "Provides:       bundled(golang("$1")) = "$2}' >> provides.spec.inc

cat << EOF >> provides.spec.inc
# grep -v -e '^$' -e '^#' moby-${version}/vendor/github.com/docker/distribution/vendor.conf | sort | awk '{print "Provides:       bundled(golang("\$1")) = "\$2}'
EOF

grep -v -e '^$' -e '^#' "moby-${version}/vendor/github.com/docker/distribution/vendor.conf" | sort | awk '{print "Provides:       bundled(golang("$1")) = "$2}' >> provides.spec.inc

# Note(gotmax23): Ignore this also. My script commits the specfile,
# and then this ammends that commit to add the updated provides.spec.inc.
if command -v update.sh && [ "$#" -gt 0 ]; then
    git add provides.spec.inc
    git commit --gpg-sign --amend --no-edit
fi
