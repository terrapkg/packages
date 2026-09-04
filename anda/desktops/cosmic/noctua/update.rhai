rpm.global("commit", codeberg_commit("wfx/noctua"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
