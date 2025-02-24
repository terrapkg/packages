rpm.global("commit", gh_commit("atar-axis/xpadneo"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let ver = gh("atar-axis/xpadneo");
    ver.crop(1);
    rpm.global("ver", ver);
}
