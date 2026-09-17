rpm.global("commit", gh_commit("CanadaHonk/porffor"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
