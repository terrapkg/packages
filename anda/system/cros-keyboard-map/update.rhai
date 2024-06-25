if filters.contains("nightly") {
  rpm.global("commit", gh_commit("WeirdTreeThing/cros-keyboard-map"));
  if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
  }
}
