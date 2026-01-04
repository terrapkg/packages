rpm.global("commit", gh_commit("FrederykAbryan/multi-monitors-bar_fapv2"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
