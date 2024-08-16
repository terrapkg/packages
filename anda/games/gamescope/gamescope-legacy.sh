#!/bin/sh

# Wrapper script to run Gamescope with legacy options for older GPUs

gamescope_path="/usr/bin/gamescope"


# Extra configuration for the people who need it, at $XDG_CONFIG_HOME/gamescope/legacy.conf or /etc/gamescope/legacy.conf
# Should import an GAMESCOPE_LEGACY_ARGS variable
# 
# We should document this in Fyra Devdocs later


if [ -f "$XDG_CONFIG_HOME/gamescope/legacy.conf" ]; then
    . "$XDG_CONFIG_HOME/gamescope/legacy.conf"
elif [ -f "/etc/gamescope/legacy.conf" ]; then
    . "/etc/gamescope/legacy.conf"
else
    GAMESCOPE_LEGACY_ARGS=""
fi


# Check if we have a $DISPLAY variable, because if not then we're probably not
# running nested

if [ -z "$DISPLAY" ]; then
    $gamescope_path --backend=drm --expose-wayland $GAMESCOPE_LEGACY_ARGS $@
else
    $gamescope_path --backend=sdl $GAMESCOPE_LEGACY_ARGS $@
fi

