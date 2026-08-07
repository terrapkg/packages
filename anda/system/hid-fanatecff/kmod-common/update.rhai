rpm.global("commit", gh_commit("gotzl/hid-fanatecff"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let ver = gh("gotzl/hid-fanatecff");
    ver.crop(0);
    rpm.global("ver", ver);
}
