rpm.global("commit", gh_commit("acxz/pokeshell"));
if rpm.changed() {
    rpm.release();
    rpm.global("date", date());
    let v = gh_tag("acxz/pokeshell");
    v.crop(1);
    rpm.global("ver", v);
}
