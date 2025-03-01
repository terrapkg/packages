rpm.global("commit", gh_commit("vinceliuice/Fluent-kde"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
