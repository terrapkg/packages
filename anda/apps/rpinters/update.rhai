rpm.global("commit", gh_commit("raspberrypi-ui/rpinters"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
