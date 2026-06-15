rpm.global("commit", gh_commit("fluxerapp/fluxer"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
