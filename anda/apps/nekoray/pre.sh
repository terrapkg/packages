export sourcedir="$PWD"
rpmdev-spectool --all --get-files nekoray.spec
version=$(rpmspec --query --queryformat "%{VERSION}\n" nekoray.spec | uniq)

tar -xzf "nekoray-${version}.tar.gz"
pushd "nekoray-${version}/core/server"
 go mod download github.com/stretchr/testify 
 go mod vendor
 tar -czf "${sourcedir}/vendor-${version}.tar.gz" vendor
popd
