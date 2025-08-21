export sourcedir="$PWD"
rpmdev-spectool --all --get-files throne.spec
version=$(rpmspec --query --queryformat "%{VERSION}\n" throne.spec | uniq)

tar -xzf "throne-${version}.tar.gz"
pushd "Throne-${version}/core/server"
 go mod download github.com/stretchr/testify 
 go mod vendor
 tar -czf "${sourcedir}/vendor-${version}.tar.gz" vendor
popd
