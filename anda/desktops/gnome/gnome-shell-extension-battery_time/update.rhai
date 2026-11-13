rpm.global("commit", gh_commit("Owen-sz/battery_time"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
