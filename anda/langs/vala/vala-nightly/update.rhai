if filters.contains("nightly") {
	rpm.global("commit", gitlab_commit("gitlab.gnome.org", "1551", "main"));
	if rpm.changed() {
		rpm.global("commit_date", date());
		rpm.release();
	}
}
