if filters.contains("nightly") {
  rpm.global("commit", gh_commit("WeirdTreeThing/chromebook-linux-audio"));
  if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
  }
}
