rpm.global("commit", gitlab_commit("gitlab.com", "46446166", "main"));
if rpm.changed() {
	rpm.global("commit_date", date());
	rpm.release();
}
