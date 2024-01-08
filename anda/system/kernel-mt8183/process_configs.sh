#!/bin/bash
#
# This script takes the merged config files and processes them through oldconfig
# and listnewconfig
#
# Globally disable suggestion of appending '|| exit' or '|| return' to cd/pushd/popd commands
# shellcheck disable=SC2164

test -n "$RHTEST" && exit 0

usage()
{
	# alphabetical order please
	echo "process_configs.sh [ options ] package_name kernel_version"
	echo "     -a: report all errors, equivalent to [-c -n -w -i]"
	echo "     -c: error on mismatched config options"
	echo "     -i: continue on error"
	echo "     -n: error on unset config options"
	echo "     -t: test run, do not overwrite original config"
	echo "     -w: error on misconfigured config options"
	echo "     -z: commit new configs to pending directory"
	echo ""
	echo "     A special CONFIG file tag, process_configs_known_broken can be added as a"
	echo "     comment to any CONFIG file.  This tag indicates that there is no way to "
	echo "     fix a CONFIG's entry.  This tag should only be used in extreme cases"
	echo "     and is not to be used as a workaround to solve CONFIG problems."
	exit 1
}

die()
{
	echo "$1"
	exit 1
}

get_cross_compile()
{
	arch=$1
	if [[ "$CC_IS_CLANG" -eq 1 ]]; then
		echo "$arch"
	else
		echo "scripts/dummy-tools/"
	fi
}

# stupid function to find top of tree to do kernel make configs
switch_to_toplevel()
{
	path="$(pwd)"
	while test -n "$path"
	do
		test -e "$path"/MAINTAINERS && \
			test -d "$path"/drivers && \
			break

		path=$(dirname "$path")
	done

	test -n "$path"  || die "Can't find toplevel"
	echo "$path"
}

checkoptions()
{
	count=$3
	variant=$4

	/usr/bin/awk '

		/is not set/ {
			split ($0, a, "#");
			split(a[2], b);
			if (NR==FNR) {
				configs[b[1]]="is not set";
			} else {
				if (configs[b[1]] != "" && configs[b[1]] != "is not set")
					 print "Found # "b[1] " is not set, after generation, had " b[1] " " configs[b[1]] " in Source tree";
			}
		}

		/=/     {
			split ($0, a, "=");
			if (NR==FNR) {
				configs[a[1]]=a[2];
			} else {
				if (configs[a[1]] != "" && configs[a[1]] != a[2])
					 print "Found "a[1]"="a[2]" after generation, had " a[1]"="configs[a[1]]" in Source tree";
			}
		}
	' "$1" "$2" > .mismatches"${count}"

	checkoptions_error=false
	if test -s .mismatches"${count}"
	then
		while read -r LINE
		do
			if find "${REDHAT}"/configs -name "$(echo "$LINE" | awk -F "=" ' { print $1 } ' | awk ' { print $2 }')" -print0 | xargs -0 grep ^ | grep -q "process_configs_known_broken"; then
				# This is a known broken config.
				# See script help warning.
				checkoptions_error=false
			else
				checkoptions_error=true
				break
			fi
		done < .mismatches"${count}"

		! $checkoptions_error && return

		sed -i "1s/^/Error: Mismatches found in configuration files for ${arch} ${variant}\n/" .mismatches"${count}"
	else
		rm -f .mismatches"${count}"
	fi
}

parsenewconfigs()
{
	tmpdir=$(mktemp -d)

	# This awk script reads the output of make listnewconfig
	# and puts it into CONFIG_FOO files. Using the output of
	# listnewconfig is much easier to ensure we get the default
	# output.
        /usr/bin/awk -v BASE="$tmpdir" '
                /is not set/ {
                        split ($0, a, "#");
                        split(a[2], b);
                        OUT_FILE=BASE"/"b[1];
                        print $0 >> OUT_FILE;
                }

                /=/     {
                        split ($0, a, "=");
                        OUT_FILE=BASE"/"a[1];
                        if (a[2] == "n")
                                print "# " a[1] " is not set" >> OUT_FILE;
                        else
                                print $0 >> OUT_FILE;
                }

        ' .newoptions

	# This awk script parses the output of helpnewconfig.
	# Each option is separated between ----- markers
	# The goal is to put all the help text as a comment in
	# each CONFIG_FOO file. Because of how awk works
	# there's a lot of moving files around and catting to
	# get what we need.
        /usr/bin/awk -v BASE="$tmpdir" '
                BEGIN { inpatch=0;
			outfile="none";
                        symbol="none"; }
                /^Symbol: .*$/ {
                        split($0, a, " ");
                        symbol="CONFIG_"a[2];
                        outfile=BASE "/fake_"symbol
                }
                /-----/ {
			if (inpatch == 0) {
				inpatch = 1;
			}
                        else {
                                if (symbol != "none") {
                                    system("cat " outfile " " BASE "/" symbol " > " BASE "/tmpf");
                                    system("mv " BASE "/tmpf " BASE "/" symbol);
                                    symbol="none"
				}
                                outfile="none"
				inpatch = 0;
                        }
                }
                !/-----/ {
                        if (inpatch == 1 && outfile != "none") {
                                print "# "$0 >> outfile;
                        }
                }


        ' .helpnewconfig

	pushd "$tmpdir" &> /dev/null
	rm fake_*
	popd &> /dev/null
	for f in "$tmpdir"/*; do
		[[ -e "$f" ]] || break
		cp "$f" "$SCRIPT_DIR/pending$FLAVOR/generic/"
	done

	rm -rf "$tmpdir"
}

function commit_new_configs()
{
	# assume we are in $source_tree/configs, need to get to top level
	pushd "$(switch_to_toplevel)" &>/dev/null

	for cfg in "$SCRIPT_DIR/${SPECPACKAGE_NAME}${KVERREL}"*.config
	do
		arch=$(head -1 "$cfg" | cut -b 3-)
		cfgtmp="${cfg}.tmp"
		cfgorig="${cfg}.orig"
		cat "$cfg" > "$cfgorig"

		if [ "$arch" = "EMPTY" ]
		then
			# This arch is intentionally left blank
			continue
		fi
		echo -n "Checking for new configs in $cfg ... "

		# shellcheck disable=SC2086
		make ${MAKEOPTS} ARCH="$arch" CROSS_COMPILE="$(get_cross_compile "$arch")" KCONFIG_CONFIG="$cfgorig" listnewconfig >& .listnewconfig
		grep -E 'CONFIG_' .listnewconfig > .newoptions
		if test -s .newoptions
		then
		# shellcheck disable=SC2086
			make ${MAKEOPTS} ARCH="$arch" CROSS_COMPILE="$(get_cross_compile "$arch")" KCONFIG_CONFIG="$cfgorig" helpnewconfig >& .helpnewconfig
			parsenewconfigs
		fi
		rm .newoptions
		echo "done"
	done

	git add "$SCRIPT_DIR/pending$FLAVOR"
	git commit -m "[redhat] AUTOMATIC: New configs"
}

function process_config()
{
	local cfg
	local arch
	local cfgtmp
	local cfgorig
	local count
	local variant

	cfg=$1
	count=$2

	arch=$(head -1 "$cfg" | cut -b 3-)

	if [ "$arch" = "EMPTY" ]
	then
		# This arch is intentionally left blank
		return
	fi

	variant=$(basename "$cfg" | cut -d"-" -f3- | cut -d"." -f1)

	cfgtmp="${cfg}.tmp"
	cfgorig="${cfg}.orig"
	cat "$cfg" > "$cfgorig"

	echo "Processing $cfg ... "

	# shellcheck disable=SC2086
	make ${MAKEOPTS} ARCH="$arch" CROSS_COMPILE="$(get_cross_compile "$arch")" KCONFIG_CONFIG="$cfgorig" listnewconfig >& .listnewconfig"${count}"
	grep -E 'CONFIG_' .listnewconfig"${count}" > .newoptions"${count}"
	if test -n "$NEWOPTIONS" && test -s .newoptions"${count}"
	then
		echo "Found unset config items in ${arch} ${variant}, please set them to an appropriate value" >> .errors"${count}"
		cat .newoptions"${count}" >> .errors"${count}"
		rm .newoptions"${count}"
		RETURNCODE=1
	fi
	rm -f .newoptions"${count}"

	grep -E 'config.*warning' .listnewconfig"${count}" > .warnings"${count}"
	if test -n "$CHECKWARNINGS" && test -s .warnings"${count}"
	then
		echo "Found misconfigured config items in ${arch} ${variant}, please set them to an appropriate value" >> .errors"${count}"
		cat .warnings"${count}" >> .errors"${count}"
	fi
	rm .warnings"${count}"

	rm .listnewconfig"${count}"

	# shellcheck disable=SC2086
	make ${MAKEOPTS} ARCH="$arch" CROSS_COMPILE="$(get_cross_compile "$arch")" KCONFIG_CONFIG="$cfgorig" olddefconfig > /dev/null || exit 1
	echo "# $arch" > "$cfgtmp"
	cat "$cfgorig" >> "$cfgtmp"
	if test -n "$CHECKOPTIONS"
	then
		checkoptions "$cfg" "$cfgtmp" "$count" "$variant"
	fi
	# if test run, don't overwrite original
	if test -n "$TESTRUN"
	then
		rm -f "$cfgtmp"
	else
		mv "$cfgtmp" "$cfg"
	fi
	rm -f "$cfgorig"
	echo "Processing $cfg complete"
}

function process_configs()
{
	# assume we are in $source_tree/configs, need to get to top level
	pushd "$(switch_to_toplevel)" &>/dev/null

	# The next line is throwaway code for transition to parallel
	# processing.  Leaving this line in place is harmless, but it can be
	# removed the next time anyone updates this function.
	[ -f .mismatches ] && rm -f .mismatches

	count=0
	for cfg in "$SCRIPT_DIR/${SPECPACKAGE_NAME}${KVERREL}"*.config
	do
		if [ "$count" -eq 0 ]; then
			# do the first one by itself so that tools are built
			process_config "$cfg" "$count"
		fi
		process_config "$cfg" "$count" &
		# shellcheck disable=SC2004
		waitpids[${count}]=$!
		((count++))
		while [ "$(jobs | grep -c Running)" -ge "$RHJOBS" ]; do :; done
	done
	# shellcheck disable=SC2048
	for pid in ${waitpids[*]}; do
		wait "${pid}"
	done

	rm "$SCRIPT_DIR"/*.config*.old

	if ls .errors* 1> /dev/null 2>&1; then
		RETURNCODE=1
		cat .errors*
		rm .errors* -f
	fi
	if ls .mismatches* 1> /dev/null 2>&1; then
		RETURNCODE=1
		cat .mismatches*
		rm .mismatches* -f
	fi

	popd > /dev/null

	[ $RETURNCODE -eq 0 ] && echo "Processed config files are in $SCRIPT_DIR"
}

CHECKOPTIONS=""
NEWOPTIONS=""
TESTRUN=""
CHECKWARNINGS=""
MAKEOPTS=""
CC_IS_CLANG=0

RETURNCODE=0

while [[ $# -gt 0 ]]
do
	key="$1"
	case $key in
		-a)
			CHECKOPTIONS="x"
			NEWOPTIONS="x"
			CHECKWARNINGS="x"
			;;
		-c)
			CHECKOPTIONS="x"
			;;
		-h)
			usage
			;;
		-n)
			NEWOPTIONS="x"
			;;
		-t)
			TESTRUN="x"
			;;
		-w)
			CHECKWARNINGS="x"
			;;
		-z)
			COMMITNEWCONFIGS="x"
			;;
		-m)
			shift
			if [ "$1" = "CC=clang" ] || [ "$1" = "LLVM=1" ]; then
				CC_IS_CLANG=1
			fi
			MAKEOPTS="$MAKEOPTS $1"
			;;
		*)
			break;;
	esac
	shift
done

KVERREL="$(test -n "$1" && echo "-$1" || echo "")"
FLAVOR="$(test -n "$2" && echo "-$2" || echo "-rhel")"
# shellcheck disable=SC2015
SCRIPT=$(readlink -f "$0")
SCRIPT_DIR=$(dirname "$SCRIPT")

# Config options for RHEL should target the pending-rhel directory, not pending-common.
if [ "$FLAVOR" = "-rhel" ]
then
	FLAVOR="-rhel"
fi

# to handle this script being a symlink
cd "$SCRIPT_DIR"

if test -n "$COMMITNEWCONFIGS"; then
	commit_new_configs
else
	process_configs
fi

exit $RETURNCODE
