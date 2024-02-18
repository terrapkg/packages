if filters.contains("nightly") {
	rpm.global("commit", gh_commit("vala-lang/vala-lint"));
	if rpm.changed() {
		rpm.global("commit_date", date());
		rpm.release();
	}
}
