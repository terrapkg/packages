rpm.global("commit", gitlab_commit("35523198", "master"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
rpm.global("latest_stable_version", gitlab_tag("35523198"));
