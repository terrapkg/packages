rpm.global("commit", gh_commit("StardustXR/magnetar"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}