rpm.global("commit", gh_commit("raspberrypi/utils"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}