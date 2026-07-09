let ver = gh_tag("albfan/miraclecast");
ver.crop(1);
rpm.global("ver", ver);

rpm.global("commit", gh_commit("albfan/miraclecast"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
