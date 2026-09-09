rpm.global("commit", gh_commit("https://github.com/inteliwear/sidepulse"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
