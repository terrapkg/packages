rpm.global("commit", gh_commit("python/typeshed"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
