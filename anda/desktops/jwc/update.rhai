rpm.global("commit", sourcehut_commit("~jsnr/jwc"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
