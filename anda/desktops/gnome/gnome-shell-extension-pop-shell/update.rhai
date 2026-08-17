if filters.contains("nightly") {
  rpm.global("commit", gh_commit("pop-os/shell"));
  if rpm.changed() {
    rpm.global("ver", gh("pop-os/shell"));
    rpm.release();
    rpm.global("commit_date", date());
  }
}
