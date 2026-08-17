rpm.global("commit", gh_commit("StardustXR/gravity"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}