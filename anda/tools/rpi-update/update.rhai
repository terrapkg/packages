rpm.global("commit", gh_commit("raspberrypi/rpi-update"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
