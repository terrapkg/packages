rpm.global("commit", gh_commit("rainer042/geteltorito"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}