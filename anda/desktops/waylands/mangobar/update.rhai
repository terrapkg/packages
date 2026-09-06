rpm.global("commit", gh_commit("Gur0v/mangobar"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
