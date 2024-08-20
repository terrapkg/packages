#!/bin/sh

# Wrapper script to run Gamescope with legacy options for older GPUs

gamescope_path="/usr/bin/gamescope"


# check if $BACKEND is already defined
# todo: Probably want to patch gamescope-session-plus for this instead meow
LEGACY_BACKEND_ARGS=""
if [ -z "$BACKEND" ]; then
    LEGACY_BACKEND_ARGS="--backend=sdl"
fi

if [ -z "$DISPLAY" ]; then
    $gamescope_path $LEGACY_BACKEND_ARGS $@
else
    $gamescope_path $LEGACY_BACKEND_ARGS $@
fi

