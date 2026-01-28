let v = bump::bodhi("alsa-lib", bump::as_bodhi_ver(labels.branch));
rpm.global("version_alsa_ucm", v)
if rpm.changed() {
    rpm.global("version_alsa_lib", v)
    rpm.global("version_tree_ucm", gh("WeirdTreeThing/alsa-ucm-conf-cros"));
}
