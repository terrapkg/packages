terminate();
rpm.global("commit", gh_commit("flameshot-org/flameshot"));
if rpm.changed() {
    let v = gh("flameshot-org/flameshot");
    v.crop(1);
    rpm.global("ver", v);
    rpm.global("commit_date", date());
}
