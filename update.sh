#!/bin/bash

search() {
    for folder in $1/*; do
        if [ -f "$folder/chkupdate.py" ]; then
            echo :: $folder
            (cd $folder && python chkupdate.py)
            continue
        fi
        x=0
        for thing in $folder/*; do
            [[ -f $thing ]] && x=1 && break
        done
        [[ $x -eq 1 ]] && search $folder
    done
}

search anda
