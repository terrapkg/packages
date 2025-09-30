rpm.global("commit", gh_commit("ManrajGrover/py-spinners"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
