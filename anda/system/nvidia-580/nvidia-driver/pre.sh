#!/bin/bash -x

# We are going to assume we already have andax installed

export VERSION=$(anda run andax/nvidia_driver_print.rhai)

SCRIPT_DIR=$(realpath $(dirname $0))

$SCRIPT_DIR/nvidia-generate-tarballs.sh