rpm.global("commit", gh_commit("xkevio/BMPtoASCII"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
