rpm.global("commit", gh_commit("XTLS/Xray-core"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("XTLS/Xray-core");
    rpm.global("ver", v);
}