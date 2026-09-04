rpm.global("ver", gh("melonDS-emu/melonDS"));

rpm.global("commit", gh_commit("melonDS-emu/melonDS"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
