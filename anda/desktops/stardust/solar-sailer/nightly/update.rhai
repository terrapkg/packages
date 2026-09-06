rpm.global("commit", gh_commit("StardustXR/solar-sailer"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
