rpm.global("commit", gh_commit("dlundqvist/xone"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    rpm.global("ver", gh("dlundqvist/xone"));
}
