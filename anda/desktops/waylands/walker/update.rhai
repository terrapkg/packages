rpm.global("upstream_version", gh("abenz1267/walker"));
if rpm.changed() {
    rpm.release();
}
