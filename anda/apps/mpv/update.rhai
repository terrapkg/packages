if filters.contains("nightly") {
	let o = req("https://api.github.com/repos/mpv-player/mpv/commits/HEAD").json();
	rpm.global("commit", o.sha);
	rpm.global("ver", gh("mpv-player/mpv"));
	rpm.release();
}
