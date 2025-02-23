rpm.global("commit_hash", gh_commit("zyedidia/micro"));
if rpm.changed() {
    rpm.global("commit_date", date());
    rpm.global("ver", gh("zyedidia/micro"));
}
