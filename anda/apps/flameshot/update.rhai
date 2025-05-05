rpm.global("commit", gh_commit("flameshot-org/flameshot"));
if rpm.changed() {
    rpm.global("ver", gh("flameshot-org/flameshot"));
    rpm.global("commit_date", date());
}
