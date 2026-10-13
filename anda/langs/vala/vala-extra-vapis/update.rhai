rpm.global("commit", gitlab_commit("gitlab.gnome.org", "1746", "master"));
if rpm.changed() {
  rpm.global("commit_date", date());
  rpm.release();
}
