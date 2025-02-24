#!/bin/bash -x

curl https://www.microsoft.com/en-us/legal/terms-of-use -o $(realpath $(dirname $0))/EULA
