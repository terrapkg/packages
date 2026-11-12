rpm.global("ver", gh("ShadowBlip/InputPlumber"));
rpm.global("commit", gh_commit("ShadowBlip/InputPlumber"));

if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
