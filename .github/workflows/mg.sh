if $1; then
	dirs=${$2/\/pkg/}
	export p="{\"id\":\"$5\",\"verl\":\"%v\",\"arch\":\"$4\",\"dirs\":\"$dirs\"}"
else
	export p="{\"id\":\"$5\",\"verl\":\"%v\",\"arch\":\"$4\"}"
fi
for f in anda-build/rpm/rpms/*; do
	n=$(lesspipe.sh $f | grep -E "Name\s*: " | sed "s@Name\s*: @@")
	v=$(echo ${f/${n}-/} | sed -E "s@\.fc$3.+@@")
	curl -H "Authorization: Bearer $6" https://madoguchi.fyralabs.com/ci/terra$3/builds/$n -X PUT -H "Content-Type: application/json" -d ${p/%v/$v} --fail-with-body &
done
wait
