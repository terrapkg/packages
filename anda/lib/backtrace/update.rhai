rpm.global("commit", gh_commit("ianlancetaylor/libbacktrace"));
if rpm.changed() {
    rpm.global("commit_date", date());
    rpm.release();
}
