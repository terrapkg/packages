version="$(rpmspec --query nekoray.spec --queryformat '%{VERSION}\n' | uniq)"
rpmdev-spectool --all --get-files nekoray.spec

tar -xzf "nekoray-${version}.tar.gz"

pushd "nekoray-${version}/core/server"
go mod vendor
tar -czf "$(rpm --eval '%{_sourcedir}')/vendor-${version}.tar.gz" vendor
popd

