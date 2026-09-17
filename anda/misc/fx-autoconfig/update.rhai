rpm.global("commit", gh_commit("MrOtherGuy/fx-autoconfig"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
