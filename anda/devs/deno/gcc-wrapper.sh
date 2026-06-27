#!/bin/bash
if [[ " $@ " =~ "jitterentropy" ]]; then
	exec gcc $(echo "$@" | sed 's/-O[0-9s]//g')
else
	exec gcc "$@"
fi
