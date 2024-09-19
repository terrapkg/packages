rpm.global("commit", gh_commit("StardustXR/atmosphere"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}