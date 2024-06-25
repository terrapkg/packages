if filters.contains("nightly") {
	rpm.global("commit", gh_commit("tdlib/td"));
	if rpm.changed() {
		let v = find("\nproject\\(TDLib\\s+VERSION\\s+([\\d.]+)\\s+", gh_rawfile("tdlib/td", "master", "CMakeLists.txt"), 1);
		rpm.global("ver", v);
		rpm.release();
	}
}
