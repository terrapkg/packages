rpm.global("commit", gh_commit("StardustXR/non-spacial-input"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
