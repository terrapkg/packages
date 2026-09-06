rpm.global("commit", gh_commit("pomoke/battery_time"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
