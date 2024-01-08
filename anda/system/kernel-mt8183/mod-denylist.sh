#! /bin/bash
# shellcheck disable=SC2164

RpmDir=$1
ModDir=$2
Dir="$1/$2"
# Note the list filename must have the format mod-[PACKAGE].list, for example,
# mod-internal.list or mod-extra.list.  The PACKAGE is used to create a
# override directory for the modules.
List=$3
Dest="$4"

blacklist()
{
	cat > "$RpmDir/etc/modprobe.d/$1-blacklist.conf" <<-__EOF__
	# This kernel module can be automatically loaded by non-root users. To
	# enhance system security, the module is blacklisted by default to ensure
	# system administrators make the module available for use as needed.
	# See https://access.redhat.com/articles/3760101 for more details.
	#
	# Remove the blacklist by adding a comment # at the start of the line.
	blacklist $1
__EOF__
}

check_blacklist()
{
	mod=$(find "$RpmDir/$ModDir" -name "$1")
	[ ! "$mod" ] && return 0
	if modinfo "$mod" | grep -q '^alias:\s\+net-'; then
		mod="${1##*/}"
		mod="${mod%.ko*}"
		echo "$mod has an alias that allows auto-loading. Blacklisting."
		blacklist "$mod"
	fi
}

find_depends()
{
	dep=$1
	depends=$(modinfo "$dep" | sed -n -e "/^depends/ s/^depends:[ \t]*//p")
	[ -z "$depends" ] && exit
	for mod in ${depends//,/ }
	do
		match=$(grep "^$mod.ko" "$ListName")
		[ -z "$match" ] && continue
		# check if the module we are looking at is in mod-* too.
		# if so we do not need to mark the dep as required.
		mod2=${dep##*/}  # same as $(basename $dep), but faster
		match2=$(grep "^$mod2" "$ListName")
		if [ -n "$match2" ]
		then
			#echo $mod2 >> notreq.list
			continue
		fi
		echo "$mod".ko >> req.list
	done
}

foreachp()
{
	P=$(nproc)
	bgcount=0
	while read -r mod; do
		$1 "$mod" &

		bgcount=$((bgcount + 1))
		if [ $bgcount -eq "$P" ]; then
			wait -n
			bgcount=$((bgcount - 1))
		fi
	done

	wait
}

# Destination was specified on the command line
test -n "$4" && echo "$0: Override Destination $Dest has been specified."

pushd "$Dir"

OverrideDir=$(basename "$List")
OverrideDir=${OverrideDir%.*}
OverrideDir=${OverrideDir#*-}
mkdir -p "$OverrideDir"

rm -rf modnames
find . -name "*.ko" -type f > modnames
# Look through all of the modules, and throw any that have a dependency in
# our list into the list as well.
rm -rf dep.list dep2.list
rm -rf req.list req2.list
touch dep.list req.list
cp "$List" .

# This variable needs to be exported because it is used in sub-script
# executed by xargs
ListName=$(basename "$List")
export ListName

foreachp find_depends < modnames

sort -u req.list > req2.list
sort -u "$ListName" > modules2.list
join -v 1 modules2.list req2.list > modules3.list

while IFS= read -r mod
do
    # get the path for the module
    modpath=$(grep /"$mod" modnames)
    [ -z "$modpath" ] && continue
    echo "$modpath" >> dep.list
done < modules3.list

sort -u dep.list > dep2.list

if [ -n "$Dest" ]; then
    # now move the modules into the $Dest directory
    while IFS= read -r mod
    do
	newpath=$(dirname "$mod" | sed -e "s/kernel\\//$Dest\//")
	mkdir -p "$newpath"
	mv "$mod" "$newpath"
	echo "$mod" | sed -e "s/kernel\\//$Dest\//" | sed -e "s|^.|${ModDir}|g" >> "$RpmDir"/"$ListName"
    done < dep2.list
fi

popd

if [ -z "$Dest" ]; then
	sed -e "s|^.|${ModDir}|g" "$Dir"/dep2.list > "$RpmDir/$ListName"
	echo "$RpmDir/$ListName created."
	[ -d "$RpmDir/etc/modprobe.d/" ] || mkdir -p "$RpmDir/etc/modprobe.d/"
	foreachp check_blacklist < "$List"
fi

# Many BIOS-es export a PNP-id which causes the floppy driver to autoload
# even though most modern systems don't have a 3.5" floppy driver anymore
# this replaces the old die_floppy_die.patch which removed the PNP-id from
# the module

floppylist=("$RpmDir"/"$ModDir"/kernel/drivers/block/floppy.ko*)
if [[ -n ${floppylist[0]} && -f ${floppylist[0]} ]]; then
     blacklist "floppy"
fi

# avoid an empty kernel-extra package
echo "$ModDir/$OverrideDir" >> "$RpmDir/$ListName"

pushd "$Dir"
rm modnames dep.list dep2.list req.list req2.list
rm "$ListName" modules2.list modules3.list
popd
