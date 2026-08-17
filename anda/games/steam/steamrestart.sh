#!/usr/bin/bash
if [[ ! -z $(ps aux | grep "steam.sh" | grep -v color | grep -v grep) ]]; then
	touch /tmp/steamrestart
        steam -shutdown  > /dev/null 2>&1 &
        while [[ ! -z $(ps aux | grep "steam.sh" | grep -v color | grep -v grep) ]]; do
                sleep 1
        done
fi
