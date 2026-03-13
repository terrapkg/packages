rpm.global("commit", gh_commit("v2rayA/v2rayA"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("v2rayA/v2rayA");
    rpm.global("ver", v);
}