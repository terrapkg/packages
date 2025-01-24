rpm.global("commit", gitlab_commit("gitlab.gnome.org", "20397", "main"));
if rpm.changed {
    rpm.global("commit_date", date());
    rpm.release();
}
