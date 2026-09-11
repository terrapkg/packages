rpm.global("commit", gitlab_commit("28721344", "main"));
if rpm.changed() {
	rpm.global("commit_date", date());
	rpm.release();
}
