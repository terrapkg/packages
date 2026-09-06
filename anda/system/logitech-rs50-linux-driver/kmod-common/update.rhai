rpm.global("commit", gh_commit("mescon/logitech-rs50-linux-driver"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
}
