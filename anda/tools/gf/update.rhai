rpm.global("commit", gh_commit("nakst/gf"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
