if filters.contains("nightly") {
  rpm.global("tree_commit", gh_commit("WeirdTreeThing/cros-keyboard-map"));
  rpm.global("um_commit", gh_commit("Ultramarine-Linux/cros-keyboard-map"));
  if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
  }
}
