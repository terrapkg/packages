#!/bin/sh
electron=/usr/bin/electron

CONFIG=${XDG_CONFIG_HOME:-~/.config}
FLAGS="$CONFIG/armcord-flags.conf"

# Allow users to override command-line options
if [ -f "$FLAGS" ]; then
  USER_FLAGS="$(cat "$FLAGS")"
fi

# shellcheck disable=SC2086 # USER_FLAGS has to be unquoted
"$electron" /usr/share/armcord/app.asar $USER_FLAGS "$@"
