rpm.global("commit", gh_commit("Nakildias/sc0710"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
}
