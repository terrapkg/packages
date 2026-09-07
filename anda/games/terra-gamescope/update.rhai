rpm.global("commit", gh_commit("OpenGamingCollective/gamescope"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
