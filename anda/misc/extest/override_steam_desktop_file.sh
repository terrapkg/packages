#!/bin/bash -x
EXTEST="/usr/lib/extest/libextest.so"
STEAM_DESKTOP_FILE="/usr/share/applications/steam.desktop"

if ! [ -f $STEAM_DESKTOP_FILE ]; then
	echo "Could not find Steam's desktop file, is XDG_DATA_DIRS	set properly?"
	exit 1
fi

sed -i "s,Exec=/usr/bin/steam,Exec=env LD_PRELOAD=$EXTEST /usr/bin/steam," $STEAM_DESKTOP_FILE

echo $STEAM_DESKTOP_FILE
echo "Extest has been set up, enjoy!"