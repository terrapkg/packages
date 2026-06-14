rpm.global("commit", gh_commit("berarma/new-lg4ff"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let ver = gh("berarma/new-lg4ff");
    ver.crop(1);
    rpm.global("ver", ver);
}
