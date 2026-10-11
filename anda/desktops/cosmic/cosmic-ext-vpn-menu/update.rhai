rpm.global("commit", gh_commit("takilazy/cosmic-ext-vpn-menu"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
