if filters.contains("nightly") {
	rpm.global("commit", gh_commit("mpv-player/mpv"));
	if rpm.changed() {
		rpm.global("ver", gh("mpv-player/mpv"));
		rpm.global("commit_date", date());
		rpm.release();
	}
}
