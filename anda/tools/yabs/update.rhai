rpm.global("commit", gh_commit("masonr/yet-another-bench-script"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
