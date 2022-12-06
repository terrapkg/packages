search() {
    for folder in $1/*; do
        if [ -f "$folder/update.rhai" ]; then
            continue
        else
            echo $folder
        fi
        x=0
        for thing in $folder/*; do
            [[ -f $thing ]] && x=1 && break
        done
        [[ $x -eq 0 ]] && search $folder
    done
}

search anda
