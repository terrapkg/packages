rpm.global("commit", gh_commit("kachick/chawan"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
