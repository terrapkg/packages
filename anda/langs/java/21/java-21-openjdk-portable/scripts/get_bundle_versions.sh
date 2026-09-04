#!/usr/bin/env sh

# Copyright (C) 2025 Red Hat, Inc.
# Original written by Antonio Vieiro <avieirov@redhat.com>
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

if [ $# -ne 1 ]; then
    echo "Usage: $0 openjdk-root-directory"
    exit 1
fi

JDKROOT=$1

if [ ! -d "${JDKROOT}" ] ; then
    echo "${JDKROOT} is not a directory.";
    exit 2
fi

# Work out the OpenJDK version
# OpenJDK >= 10 has its version in the build machinery
# OpenJDK >= 17 stores it in a new location (JDK-8258246)
VERSION_FILE="${JDKROOT}"/make/conf/version-numbers.conf
printf "Checking for %s..." "${VERSION_FILE}";
if [ ! -f "${VERSION_FILE}" ] ; then
    VERSION_FILE="${JDKROOT}"/make/autoconf/version-numbers
    echo "Not found; using old version file ${VERSION_FILE}";
else
    echo "found.";
fi
if [ -e "${VERSION_FILE}" ] ; then
    openjdk_version=$(grep '^DEFAULT_VERSION_FEATURE' "${VERSION_FILE}" | cut -d '=' -f 2)
elif [ -e "${JDKROOT}"/jdk/src/java.base/share/classes/java/lang/Object.java ] ; then
    openjdk_version=9;
elif [ -e "${JDKROOT}"/common/autoconf ] ; then
    openjdk_version=8;
else
    openjdk_version=7;
fi
echo "OpenJDK version: ${openjdk_version}";

#
# Freetype
#
if [ "${openjdk_version}" -gt 8 ] ; then
    FREETYPE=src/java.desktop/share/native/libfreetype/include/freetype/freetype.h
    ABS_FREETYPE="${JDKROOT}"/"${FREETYPE}"
    if [ ! -f "${ABS_FREETYPE}" ]; then
        echo "Freetype header not found!"
        exit 2
    fi
    FREETYPE_VERSION=$(awk '/#define FREETYPE_MAJOR/ {MAJOR=$3} /#define FREETYPE_MINOR/ {MINOR=$3} /#define FREETYPE_PATCH/ {PATCH=$3} END {printf "%s.%s.%s", MAJOR, MINOR, PATCH}' "${ABS_FREETYPE}")
else
    echo "No bundled FreeType on ${openjdk_version}";
fi

# giflib
if [ "${openjdk_version}" -gt 8 ] ; then
    GIFLIB=src/java.desktop/share/native/libsplashscreen/giflib/gif_lib.h
else
    GIFLIB=jdk/src/share/native/sun/awt/giflib/gif_lib.h
fi
ABS_GIFLIB="${JDKROOT}"/"${GIFLIB}"
if [ ! -f "${ABS_GIFLIB}" ]; then
    echo "giflib header not found!"
    exit 3
fi
GIFLIB_VERSION=$(awk '/#define GIFLIB_MAJOR/ {MAJOR=$3} /#define GIFLIB_MINOR/ {MINOR=$3} /#define GIFLIB_RELEASE/ {PATCH=$3} END {printf "%s.%s.%s", MAJOR, MINOR, PATCH}' "${ABS_GIFLIB}")

# harfbuzz
if [ "${openjdk_version}" -gt 8 ] ; then
    HARFBUZZ=src/java.desktop/share/native/libharfbuzz/hb-version.h
    ABS_HARFBUZZ="${JDKROOT}/${HARFBUZZ}"
    if [ ! -f "${ABS_HARFBUZZ}" ]; then
        echo "HarfBuzz header not found!"
        exit 4
    fi
    HARFBUZZ_VERSION=$(awk '/#define HB_VERSION_MAJOR/ {MAJOR=$3} /#define HB_VERSION_MINOR/ {MINOR=$3} /#define HB_VERSION_MICRO/ {PATCH=$3} END {printf "%s.%s.%s", MAJOR, MINOR, PATCH}' "${ABS_HARFBUZZ}")
else
    echo "No HarfBuzz on ${openjdk_version}";
fi

# lcms
if [ "${openjdk_version}" -gt 8 ] ; then
    LCMS=src/java.desktop/share/native/liblcms/lcms2.h
else
    LCMS=jdk/src/share/native/sun/java2d/cmm/lcms/lcms2.h
fi
ABS_LCMS="${JDKROOT}"/"${LCMS}"
if [ ! -f "${ABS_LCMS}" ]; then
    echo "lcms header not found!"
    exit 5
fi
LCMS_VERSION=$(awk '/#define LCMS_VERSION/ { MAJOR=int($3 / 1000); REST=$3 % 1000; MINOR=int(REST / 10); PATCH=REST % 10; } END {printf "%s.%s.%s", MAJOR, MINOR, PATCH}' "${ABS_LCMS}")

# jpeg
if [ "${openjdk_version}" -gt 8 ] ; then
    JPEG=src/java.desktop/share/native/libjavajpeg/jpeglib.h
else
    JPEG=jdk/src/share/native/sun/awt/image/jpeg/jpeglib.h
fi
ABS_JPEG="${JDKROOT}"/"${JPEG}"
if [ ! -f "${ABS_JPEG}" ]; then
    echo "jpeg header not found!"
    exit 6
fi
JPEG_VERSION=$(awk '/#define JPEG_LIB_VERSION/ { VERSION=$3; MAJOR=int(VERSION / 10); MINOR=VERSION%10; } END {printf "%s%c", MAJOR, (MINOR+96)}' "${ABS_JPEG}")

# png
if [ "${openjdk_version}" -gt 8 ] ; then
    PNG=src/java.desktop/share/native/libsplashscreen/libpng/png.h
else
    PNG=jdk/src/share/native/sun/awt/libpng/png.h
fi
ABS_PNG="${JDKROOT}"/"${PNG}"
if [ ! -f "${ABS_PNG}" ]; then
    echo "png header not found!"
    exit 7
fi
PNG_VERSION=$(awk '/#define PNG_LIBPNG_VER_STRING/ { VERSION=$3; gsub("\"", "", VERSION) } END {print VERSION}' "${ABS_PNG}")

# zlib
if [ "${openjdk_version}" -gt 8 ] ; then
    ZLIB=src/java.base/share/native/libzip/zlib/zlib.h
else
    ZLIB=jdk/src/share/native/java/util/zip/zlib/zlib.h
fi
ABS_ZLIB="${JDKROOT}"/"${ZLIB}"
if [ ! -f "${ABS_ZLIB}" ]; then
    echo "zlib header not found!"
    exit 8
fi
ZLIB_VERSION=$(awk '/#define ZLIB_VERSION/ { VERSION=$3; gsub("\"", "", VERSION) } END {print VERSION}' "${ABS_ZLIB}")

# Print output
printf "\nRPM definitions:\n"
if [ "${openjdk_version}" -gt 8 ] ; then
    echo "# Version in ${FREETYPE}"
    echo "Provides: bundled(freetype) = ${FREETYPE_VERSION}"
fi
echo "# Version in ${GIFLIB}"
echo "Provides: bundled(giflib) = ${GIFLIB_VERSION}"
if [ "${openjdk_version}" -gt 8 ] ; then
    echo "# Version in ${HARFBUZZ}"
    echo "Provides: bundled(harfbuzz) = ${HARFBUZZ_VERSION}"
fi
echo "# Version in ${LCMS}"
echo "Provides: bundled(lcms2) = ${LCMS_VERSION}"
echo "# Version in ${JPEG}"
echo "Provides: bundled(libjpeg) = ${JPEG_VERSION}"
echo "# Version in ${PNG}"
echo "Provides: bundled(libpng) = ${PNG_VERSION}"
echo "# Version in ${ZLIB}"
echo "Provides: bundled(zlib) = ${ZLIB_VERSION}"

# Local Variables:
# compile-command: "shellcheck get_bundle_versions.sh"
# fill-column: 80
# indent-tabs-mode: nil
# sh-basic-offset: 4
# End:
