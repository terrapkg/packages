if filters.contains("nightly") {
	rpm.global("commit", gh_commit("zed-industries/zed"));
	if rpm.changed() {
		rpm.global("ver", gh("zed-industries/zed"));
		rpm.global("commit_date", date());
		rpm.release();
	}
}
