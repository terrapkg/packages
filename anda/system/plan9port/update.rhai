rpm.global("commit", gh_commit("9fans/plan9port"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
