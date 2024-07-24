set -x

dirs=$2
dirs=${dirs/\/pkg/}
export p="{\"id\":\"$5\",\"ver\":\"%v\",\"rel\":\"%r\",\"arch\":\"$4\",\"dirs\":\"$dirs\",\"succ\":$1,\"commit\":\"$6\"}"

if [[ $1 == false ]]; then
	d=${p/\%v/?}
	d=${d/\%r/?}
	curl -H "Authorization: Bearer $6" https://madoguchi.fyralabs.com/ci/terra$3/builds/f -X PUT -H "Content-Type: application/json" -d $d --fail-with-body
	exit 0
fi

for f in anda-build/rpm/rpms/*; do
	n=$(lesspipe.sh $f | grep -E "Name\s*: " | sed "s@Name\s*: @@")
	v=$(lesspipe.sh $f | grep -E "Version\s*: " | sed "s@Version\s*: @@")
	r=$(lesspipe.sh $f | grep -E "Release\s*: " | sed "s@Release\s*: @@")
	d=${p/\%v/$v}
	d=${d/\%r/$r}
	curl -H "Authorization: Bearer $6" https://madoguchi.fyralabs.com/ci5/terra$3/builds/$n -X PUT -H "Content-Type: application/json" -d $d --fail-with-body
done
