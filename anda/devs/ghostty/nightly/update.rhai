rpm.global("commit", gh_commit("ghostty-org/ghostty"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
