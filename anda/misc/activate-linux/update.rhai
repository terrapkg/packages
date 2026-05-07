rpm.global("commit", gh_commit("MrGlockenspiel/activate-linux"));
if rpm.changed() {
    rpm.release();
    rpm.global("date", date());
    let ver = gh_tag("MrGlockenspiel/activate-linux");
    ver.crop(1);
    rpm.global("ver", ver);
}
