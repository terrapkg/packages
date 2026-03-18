rpm.global("commit", gh_commit("honjow/steamos-manager", “dev”));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
