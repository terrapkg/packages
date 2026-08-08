rpm.global("latest_stable_version", gh("pingdotgg/t3code"));
rpm.global("commit", gh_commit("pingdotgg/t3code"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
