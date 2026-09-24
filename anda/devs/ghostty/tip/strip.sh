#!/usr/bin/bash

# Zig 0.16.0 mislinks certain files to absolute paths
# This causes libghostty-vt.a to link to base64.o in the path of the RPM build dir

/usr/bin/strip $* 2> /dev/null || echo -e "\e[33mWARNING:\033[0m Mislinked library found: ${10}, skipping"
