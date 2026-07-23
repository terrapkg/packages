rpm.global("commit", sourcehut_commit("~malicean/alipad"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
