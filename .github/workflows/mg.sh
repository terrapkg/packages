if $1; then
	dirs=$2
	dirs=${dirs/\/pkg/}
	export p="{\"id\":\"$5\",\"verl\":\"%v\",\"arch\":\"$4\",\"dirs\":\"$dirs\"}"
else
	export p="{\"id\":\"$5\",\"verl\":\"%v\",\"arch\":\"$4\"}"
fi
for f in anda-build/rpm/rpms/*; do
	n=$(lesspipe.sh $f | grep -E "Name\s*: " | sed "s@Name\s*: @@")
	v=$(lesspipe.sh $f | grep -E "Version\s*: " | sed "s@Version\s*: @@")
	r=$(lesspipe.sh $f | grep -E "Release\s*: " | sed "s@Release\s*: @@")
	curl -H "Authorization: Bearer $6" https://madoguchi.fyralabs.com/ci/terra$3/builds/$n -X PUT -H "Content-Type: application/json" -d ${p/\%v/$v.$r} --fail-with-body &
done
wait
