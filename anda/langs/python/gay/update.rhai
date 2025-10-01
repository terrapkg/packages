rpm.global("commit", gh_commit("ms-jpq/gay"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
