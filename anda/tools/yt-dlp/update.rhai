if filters.contains("nightly") {
	rpm.global("commit", gh_commit("yt-dlp/yt-dlp"));
	if rpm.changed() {
		rpm.global("ver", gh("yt-dlp/yt-dlp"));
		rpm.global("commit_date", date());
		rpm.release();
	}
}
