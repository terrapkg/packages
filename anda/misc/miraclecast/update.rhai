rpm.global("ver", gh_tag("albfan/miraclecast"));

rpm.global("commit", gh_commit("albfan/miraclecast"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
