rpm.global("commit", gh_commit("inteliwear/sidepulse"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
