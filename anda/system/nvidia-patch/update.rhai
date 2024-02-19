if filters.contains("nightly") {
	rpm.global("commit", gh_commit("keylase/nvidia-patch"));
	if rpm.changed() {
		rpm.global("commit_date", date());
		rpm.release();
	}
}
