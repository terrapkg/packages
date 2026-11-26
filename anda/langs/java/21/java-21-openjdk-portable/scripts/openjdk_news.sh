#!/bin/bash

# Copyright (C) 2024 Red Hat, Inc.
# Written by Andrew John Hughes <gnu.andrew@redhat.com>, 2012-2022
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

OLD_RELEASE=$1
NEW_RELEASE=$2
REPO=$3
SUBDIR=$4
SCRIPT_DIR=$(dirname "${0}")

if test "${SUBDIR}" = ""; then
    echo "No subdirectory specified; using .";
    SUBDIR=".";
fi

if test "$REPO" = ""; then
    echo "No repository specified; using ${PWD}"
    REPO=${PWD}
fi

if test "${TMPDIR}" = ""; then
    TMPDIR=/tmp;
fi

echo "Repository: ${REPO}"

if [ -e "${REPO}/.git" ] ; then
    TYPE=git;
elif [ -e "${REPO}/.hg" ] ; then
    TYPE=hg;
else
    echo "No Mercurial or Git repository detected.";
    exit 1;
fi

if test "$OLD_RELEASE" = "" || test "$NEW_RELEASE" = ""; then
    echo "ERROR: Need to specify old and new release";
    exit 2;
fi

echo "Listing fixes between $OLD_RELEASE and $NEW_RELEASE in $REPO"
rm -f "${TMPDIR}/fixes2" "${TMPDIR}/fixes3" "${TMPDIR}/fixes"
for repos in . $("${SCRIPT_DIR}/discover_trees.sh" "${REPO}");
do
    if test "$TYPE" = "hg"; then
	hg log -r "tag('$NEW_RELEASE'):tag('$OLD_RELEASE') - tag('$OLD_RELEASE')" -R "$REPO/$repos" -G -M "${REPO}/${SUBDIR}" | \
	    grep -E '^[o:| ]*summary'|grep -v 'Added tag'|sed -r 's#^[o:| ]*summary:\W*([0-9])#  - JDK-\1#'| \
	    sed 's#^[o:| ]*summary:\W*#  - #' >> "${TMPDIR}/fixes2";
	hg log -v -r "tag('$NEW_RELEASE'):tag('$OLD_RELEASE') - tag('$OLD_RELEASE')" -R "$REPO/$repos" -G -M "${REPO}/${SUBDIR}" | \
	    grep -E '^[o:| ]*[0-9]{7}'|sed -r 's#^[o:| ]*([0-9]{7})#  - JDK-\1#' >> "${TMPDIR}/fixes3";
    else
	git -C "${REPO}" log --no-merges --pretty=format:%B "${NEW_RELEASE}...${OLD_RELEASE}" -- "${SUBDIR}" |grep -E '^[0-9]{7}' | \
	    sed -r 's#^([0-9])#  - JDK-\1#' >> "${TMPDIR}/fixes2";
	touch "${TMPDIR}/fixes3" ; # unused
    fi
done

sort "${TMPDIR}/fixes2" "${TMPDIR}/fixes3" > "${TMPDIR}/fixes4"
uniq "${TMPDIR}/fixes4" > "${TMPDIR}/fixes"
rm -f "${TMPDIR}/fixes2" "${TMPDIR}/fixes3"

if ! [ -s "${TMPDIR}/fixes" ] ; then
    echo "Failed to obtain fixes.";
    exit 3;
fi

echo "In ${TMPDIR}/fixes:"
cat "${TMPDIR}/fixes"

printf "\nChecking for duplicates...";
if uniq -d "${TMPDIR}/fixes4" | grep 'JDK' > "${TMPDIR}/dupes"; then
    printf "found.\nWARNING: Review the following duplicates:\n";
    cat "${TMPDIR}/dupes";
else
    echo "No apparent duplicates.";
fi
rm -f "${TMPDIR}/fixes4";

printf "\nChecking for backouts...";
if grep -i 'backout' "${TMPDIR}/fixes" > "${TMPDIR}/backouts"; then
    printf "found.\nWARNING: Review the following backouts:\n"
    cat "${TMPDIR}/backouts";
else
    echo "No apparent backouts.";
fi
printf "\nChecking for bundled library updates...";
if grep -iE ':( \(tz\))? (update|upgrade).*(freetype|gif|harfbuzz|lcms|jpeg|png|timezone|zlib)' "${TMPDIR}/fixes" > "${TMPDIR}/bundles"; then
    printf "found.\nWARNING: Review the following with respect to bundled provides:\n";
    cat "${TMPDIR}/bundles";
    echo "Compare the output of $(dirname "${0}")/get_bundle_versions.sh with the RPM using the JDK source tree"
else
    echo "No apparent library updates.";
fi

# Local Variables:
# compile-command: "shellcheck openjdk_news.sh"
# fill-column: 80
# indent-tabs-mode: nil
# sh-basic-offset: 4
# End:
