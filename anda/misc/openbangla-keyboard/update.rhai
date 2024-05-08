if filters.contains("nightly") {
	rpm.global("commit", get("https://api.github.com/repos/OpenBangla/OpenBangla-Keyboard/commits/develop").json().sha);
	if rpm.changed() {
		rpm.global("ver", gh("OpenBangla/OpenBangla-Keyboard"));
		rpm.global("commit_date", date());
		rpm.release();
	}
}
