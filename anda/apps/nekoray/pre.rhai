let version = find(`([\d.]+)-\d+-\d+-\d+`, gh_rawfile("Mahdi-zarei/nekoray", "dev", "nekoray_version.txt"), 1);
let sourcedir = "anda/apps/nekoray";
sh(`curl https://github.com/Mahdi-zarei/nekoray/archive/refs/tags/${version}.tar.gz -o ${sourcedir}/nekoray-${version}.tar.gz`, #{});
sh(`dnf in -y golang`, #{} );
sh(`tar -xzf "${sourcedir}/nekoray-${version}.tar.gz"; pushd "nekoray-${version}/core/server"; go mod vendor; tar -czf "${sourcedir}/vendor-${version}.tar.gz" vendor; popd`, #{});
