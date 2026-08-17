if filters.contains("nightly") {
  rpm.global("commit", gh_commit("thesofproject/avsdk"));
  if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
  }
}
