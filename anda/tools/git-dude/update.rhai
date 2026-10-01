rpm.global("commit", gh_commit("ku1ik/git-dude"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
