rpm.global("commit", gh_commit("pi-top/pi-topd"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
