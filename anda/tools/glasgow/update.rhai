rpm.global("commit", gh_commit("GlasgowEmbedded/glasgow"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
