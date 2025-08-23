let sourcedir = "anda/apps/nekoray";

sh(`echo dnf in -y golang rpmdevtools tar rpm-build coreutils`, #{});
sh(`echo pushd ${sourcedir}; echo bash -x pre.sh; echo popd`, #{});

