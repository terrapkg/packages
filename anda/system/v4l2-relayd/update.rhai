rpm.global("commit", gitlab_commit("gitlab.com", "24306684", "main"));
if rpm.changed() {
	rpm.global("commit_date", date());
	rpm.release();
}
