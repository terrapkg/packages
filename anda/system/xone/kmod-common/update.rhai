rpm.global("commit", gh_commit("dlundqvist/xone"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let ver = gh_tag("dlundqvist/xone");
    ver.crop(1);
    rpm.global("ver", ver);
}
