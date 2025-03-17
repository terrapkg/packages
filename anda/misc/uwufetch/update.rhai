rpm.global("commit", gh_commit("ad-oliviero/uwufetch"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let ver = gh_tag("ad-oliviero/uwufetch");
    ver.crop(1);
    rpm.global("ver", ver);
}
