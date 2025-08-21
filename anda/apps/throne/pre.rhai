let sourcedir = "anda/apps/throne";

sh(`dnf in -y golang rpmdevtools tar rpm-build coreutils`, #{});
sh(`pushd ${sourcedir}; bash -x pre.sh; popd`, #{});

