#!/bin/bash

set -e

function show_help () {
  echo "Usage: 'ipu6-driver-select [ proprietary | foss ]'"
  exit 1
}

function needs_pipewire_restart () {
  echo "Run 'systemctl --user restart pipewire' for the changes to take effect"
  exit 0
}

if (( $# != 1 )); then
  show_help
fi

case "$1" in
  "foss")
    systemctl disable --now v4l2-relayd.service
    needs_pipewire_restart
    ;;
  "proprietary")
    systemctl enable --now v4l2-relayd.service
    needs_pipewire_restart
    ;;
  *)
    show_help
    ;;
esac
