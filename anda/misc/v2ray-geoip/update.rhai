rpm.global("commit", gh_commit("v2fly/geoip"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("v2fly/geoip");
    rpm.global("ver", v);
}