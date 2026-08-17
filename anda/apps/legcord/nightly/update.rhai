rpm.global("commit", gh_commit("Legcord/Legcord"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}