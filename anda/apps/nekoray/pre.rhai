sh(`
version="$(rpmspec --query nekoray.spec --queryformat '%{VERSION}\n' | uniq)"
rpmdev-spectool --all --get-files nekoray.spec

tar -xzf "nekoray-${version}.tar.gz"

pushd "nekoray-${version}/core/server"
go mod vendor
tar -czf "../../vendor-${version}.tar.gz" vendor
popd

curl https://api.github.com/repos/sagernet/sing-box/releases/latest | jq -r '.name' > "NekoRay-${version}.Sagernet.SingBox.Version.txt"
`)
