rpm.global("commit", gh_commit("Kimplul/hid-tmff2"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    rpm.global("ver", gh("Kimplul/hid-tmff2"));
}
