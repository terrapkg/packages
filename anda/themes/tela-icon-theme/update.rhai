rpm.global("commit", gh_commit("vinceliuice/Tela-icon-theme"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
