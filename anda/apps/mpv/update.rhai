if filters.contains("nightly") {
	rpm.global("commit", gh_commit("mpv-player/mpv"));
	if rpm.changed() {
		let v = gh("mpv-player/mpv");
		if v.starts_with("v") {
			v.crop(1);
		}
		rpm.global("ver", v);
		rpm.global("commit_date", date());
		rpm.release();
	}
}
