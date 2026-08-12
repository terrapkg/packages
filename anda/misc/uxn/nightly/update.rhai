rpm.global("commit", sourcehut_commit("~rabbits/uxn"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
