#!/usr/bin/bash

YARN_INSTALL_DIR="/usr/lib/node_modules/yarn-berry"
YARN_BIN="scripts/bin/__YARN_BIN"

cd "$YARN_INSTALL_DIR"

exec "yarn" "$@"
