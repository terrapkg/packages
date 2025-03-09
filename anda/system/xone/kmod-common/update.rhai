rpm.global("commit", gh_commit("dlundqvist/xone"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let ver = gh_tag("dlundqvist/xone");
    ver.crop(1);
    rpm.global("ver", ver);
}
