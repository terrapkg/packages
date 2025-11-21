rpm.global("commit", gh_commit("raspberrypi-ui/raindrop"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
