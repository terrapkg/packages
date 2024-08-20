#!/bin/sh

# Wrapper script to run Gamescope with legacy options for older GPUs

gamescope_path="/usr/bin/gamescope"


# check if $BACKEND is already defined
# todo: Probably want to patch gamescope-session-plus for this instead meow

# For compatibility, let's add the argument for nested backends too

LEGACY_BACKEND_ARGS=""
NESTED_BACKEND_ARGS=""
if [ -z "$BACKEND" ]; then
    LEGACY_BACKEND_ARGS="--backend=sdl"
    NESTED_BACKEND_ARGS="--backend=sdl"
else
    # Only added for nested sessions, as $BACKEND should be defined only for legacy
    NESTED_BACKEND_ARGS="--backend=$BACKEND"
fi


if [ -z "$DISPLAY" ]; then
    $gamescope_path $LEGACY_BACKEND_ARGS $@
else
    $gamescope_path $NESTED_BACKEND_ARGS $@
fi

