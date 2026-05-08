rpm.global("commit", gh_commit("raspberrypi-ui/appset"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
