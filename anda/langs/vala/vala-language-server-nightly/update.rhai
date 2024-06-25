if filters.contains("nightly") {
	rpm.global("commit", gh_commit("vala-lang/vala-language-server"));
	if rpm.changed() {
		rpm.global("commit_date", date());
		rpm.global("verrel", gh("vala-lang/vala-language-server"));
		rpm.release();
	}
}
