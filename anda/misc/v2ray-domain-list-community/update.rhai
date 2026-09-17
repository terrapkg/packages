rpm.global("commit", gh_commit("v2fly/domain-list-community"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("v2fly/domain-list-community");
    rpm.global("ver", v);
}