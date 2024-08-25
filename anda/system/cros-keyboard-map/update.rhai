if filters.contains("nightly") {
  rpm.global("tree_commit", gh_commit("WeirdTreeThing/cros-keyboard-map"));
  rpm.global("commit", gh_commit("WeirdTreeThing/cros-keyboard-map"));
  if rpm.changed() {
    rpm.release();
    rpm.global("tree_commit_date", date());
    rpm.global("um_commit_date", date());
  }
}
