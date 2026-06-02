rpm.global("commit", gh_commit("arduino/remoteocd"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
