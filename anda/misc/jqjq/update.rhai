rpm.global("commit", gh_commit("wader/jqjq"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
