if filters.contains("nightly") {
  rpm.global("commit", gh_commit("Ultramarine-Linux/duet-quirks"));
  if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
  }
}
