if filters.contains("nightly") {
  rpm.global("commit", gh_commit("Vanilla-OS/Albius"));
  if rpm.changed() {
    rpm.global("commit_date", date());
    rpm.release();
  }
}
