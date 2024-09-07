if filters.contains("nightly") {
  rpm.global("commit", gh_commit("StardustXR/armillary"));
  if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
  }
}
