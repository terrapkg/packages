rpm.global("commit", gh_commit("Winetricks/winetricks"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("Winetricks/winetricks");
    rpm.global("ver", v);
}
