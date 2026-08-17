if filters.contains("nightly") {
	rpm.global("commit", gh_commit("PrismLauncher/PrismLauncher"));
	if rpm.changed() {
		rpm.release();
		let cmake = get("https://raw.githubusercontent.com/PrismLauncher/PrismLauncher/develop/CMakeLists.txt");
		let maj = find("set\\(Launcher_VERSION_MAJOR\\s+(\\d+)\\)", cmake, 1);
		let min = find("set\\(Launcher_VERSION_MINOR\\s+(\\d+)\\)", cmake, 1);
		rpm.global("commit_date", date());
		rpm.version(`${maj}.${min}^%{snapshot_info}`);
	}
}
