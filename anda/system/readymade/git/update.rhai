rpm.global("commit", gh_commit("FyraLabs/readymade"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
