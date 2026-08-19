rpm.global("commit", gh_commit("brkzlr/libmemscan"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
