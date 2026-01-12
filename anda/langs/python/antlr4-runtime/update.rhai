rpm.global("commit", gh_commit("parrt/antlr4-python3"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("Winetricks/winetricks");
    rpm.global("ver", v);
}
