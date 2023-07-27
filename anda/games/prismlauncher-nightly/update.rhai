if filters.contains("nightly") {
	let req = new_req("https://api.github.com/repos/PrismLauncher/PrismLauncher/commits/HEAD");
	req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	let sha = req.get().json().sha;
	rpm.global("commit", sha);
	rpm.release();
	let cmake = get("https://raw.githubusercontent.com/PrismLauncher/PrismLauncher/develop/CMakeLists.txt");
	let maj = find("set\\(Launcher_VERSION_MAJOR\\s+(\\d+)\\)", cmake, 1);
	let min = find("set\\(Launcher_VERSION_MINOR\\s+(\\d+)\\)", cmake, 1);
	rpm.version(`${maj}.${min}^%{snapshot_info}`);
}
