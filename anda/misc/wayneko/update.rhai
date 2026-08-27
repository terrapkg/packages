rpm.global("commit", sourcehut_commit("~leon_plickat/wayneko"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
