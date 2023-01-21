if filters.contains("nightly") {
	let req = new_req("https://api.github.com/repos/GooseMod/OpenAsar/commits/HEAD");
	req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	let sha = req.get().json().sha;
	rpm.define("commit", sha);
	rpm.release();
}
let html = get("https://discordapp.com/api/download/canary?platform=linux&format=tar.gz");
let newver = find("https://dl-canary\\.discordapp\\.net/apps/linux/([\\.\\d]+)/", html, 1);
rpm.version(newver);
