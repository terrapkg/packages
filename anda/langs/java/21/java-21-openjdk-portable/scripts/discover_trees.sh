#!/bin/sh

# Copyright (C) 2024 Red Hat, Inc.
# Written by Andrew John Hughes <gnu.andrew@redhat.com>.
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

TREE=${1}

if test "${TREE}" = ""; then
    TREE=${PWD}
fi

if [ -e "${TREE}"/nashorn/.hg ] || [ -e "${TREE}"/nashorn/merge.changeset ] ; then
    NASHORN="nashorn" ;
fi

if [ -e "${TREE}"/corba/.hg ] || [ -e "${TREE}"/corba/merge.changeset ] ; then
    CORBA="corba";
fi

if [ -e "${TREE}"/jaxp/.hg ] || [ -e "${TREE}"/jaxp/merge.changeset ] ; then
    JAXP="jaxp";
fi

if [ -e "${TREE}"/jaxws/.hg ] || [ -e "${TREE}"/jaxws/merge.changeset ] ; then
    JAXWS="jaxws";
fi

if [ -e "${TREE}"/langtools/.hg ] || [ -e "${TREE}"/langtools/merge.changeset ] ; then
    LANGTOOLS="langtools";
fi

if [ -e "${TREE}"/jdk/.hg ] || [ -e "${TREE}"/jdk/merge.changeset ] ; then
    JDK="jdk";
fi

if [ -e "${TREE}"/hotspot/.hg ] || [ -e "${TREE}"/hotspot/merge.changeset ] ; then
    HOTSPOT="hotspot";
fi

SUBTREES="${CORBA} ${JAXP} ${JAXWS} ${LANGTOOLS} ${NASHORN} ${JDK} ${HOTSPOT}";
echo "${SUBTREES}"

# Local Variables:
# compile-command: "shellcheck discover_trees.sh"
# fill-column: 80
# indent-tabs-mode: nil
# sh-basic-offset: 4
# End:
