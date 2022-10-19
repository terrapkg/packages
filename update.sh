#!/bin/bash -x

python -m ensurepip
python -m pip install -r requirements.txt

search() {
    for folder in $1/*; do
        if [ -f "$folder/chkupdate.py" ]; then
            (cd $folder && python chkupdate.py)
            continue
        fi
        x=0
        for thing in $folder/*; do
            [[ -f $thing ]] && x=1 && break
        done
        [[ $x -eq 0 ]] && search $folder
    done
}

search anda

exit 0
