cd man
for FILE in *.md; do
    base="$(basename "$FILE")"
    name="${base%.md}"
    num="${name##*.}"
    if [ -z "$num" ] || [ "$name" = "$num" ]; then
    # skip files that aren't of the format xxxx.N.md (like README.md)
        continue
    fi
    mkdir -p "./man${num}"
    (set -x ;go-md2man -in "$FILE" -out "./man${num}/${name}")
done
