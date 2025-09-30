rpm.global("commit", gh_commit("manrajgrover/halo"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
