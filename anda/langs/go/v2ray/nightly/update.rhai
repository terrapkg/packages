rpm.global("commit", gh_commit("v2fly/v2ray-core"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("v2fly/v2ray-core");
    rpm.global("ver", v);
}