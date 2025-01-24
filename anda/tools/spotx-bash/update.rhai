rpm.global("commit", gh_commit("SpotX-Official/SpotX-Bash"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
