if filters.contains("nightly") {
	let req = new_req("https://api.github.com/repos/vala-lang/vala-language-server/commits/HEAD");
	req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	rpm.global("commit", json(req.get()).sha);
	rpm.global("verrel", gh("vala-lang/vala-language-server"));
	rpm.release();
}
