if filters.contains("nightly") {
	let req = new_req("https://api.github.com/repos/vala-lang/vala-lint/commits/HEAD");
	req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	let sha = json(req.get()).sha;
	rpm.global("commit", sha);
	rpm.release();
}
