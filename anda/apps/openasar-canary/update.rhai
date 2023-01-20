if filters.contains("nightly") {
	let req = new_req("https://api.github.com/repos/GooseMod/OpenAsar/commits/HEAD");
	req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	let sha = req.get().json().sha;
	rpm.define("commit", sha);
	rpm.release();
}
