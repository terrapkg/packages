rpm.global("commit", gh_commit("manrajgrover/py-log-symbols"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
