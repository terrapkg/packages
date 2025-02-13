#!/bin/bash

set -e

function show_help () {
  echo "Usage: 'ipu6-driver-select [ proprietary | open ]'"
  exit 1
}

function needs_reboot () {
  echo "Reboot your system for the changes to take effect"
  exit 0
}

if (( $# != 1 )); then
  show_help
fi

case "$1" in
  "open")
    echo "blacklist icamera-ipu6" > /etc/modprobe.d/ipu6-driver-select.conf
    echo "blacklist icamera-ipu6-isys" >> /etc/modprobe.d/ipu6-driver-select.conf
    echo "blacklist icamera-ipu6-psys" >> /etc/modprobe.d/ipu6-driver-select.conf
    systemctl disable v4l2-relayd.service
    needs_reboot
    ;;
  "proprietary")
    echo "blacklist intel-ipu6" > /etc/modprobe.d/ipu6-driver-select.conf
    systemctl enable v4l2-relayd.service
    needs_reboot
    ;;
  *)
    show_help
    ;;
esac
