rpm.global("commit", gh_commit("linux-msm/qdl"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
