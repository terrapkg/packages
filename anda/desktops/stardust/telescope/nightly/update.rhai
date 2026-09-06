rpm.global("commit", gh_commit("StardustXR/telescope"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
