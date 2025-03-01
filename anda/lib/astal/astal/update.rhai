rpm.global("commit", gh_commit("Aylur/astal"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
