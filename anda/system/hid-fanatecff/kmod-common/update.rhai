rpm.global("commit", gh_commit("gotzl/hid-fanatecff"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    rpm.global("ver", gh("gotzl/hid-fanatecff"));
}
