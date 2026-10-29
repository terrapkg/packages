#!/bin/bash
# Prints a short hash of everything a package build depends on in this repo:
# the package directory and the build workflow. Two builds with the same
# fingerprint are interchangeable, so a push can reuse RPMs built for its PR.
set -euo pipefail
dir=$(dirname "$1")
{
	git rev-parse "HEAD:$dir"
	git rev-parse HEAD:.github/workflows/json-build.yml
} | sha256sum | cut -c1-16
