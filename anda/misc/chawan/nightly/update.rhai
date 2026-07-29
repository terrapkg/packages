rpm.global("commit", sourcehut_commit("~bptato/chawan"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
