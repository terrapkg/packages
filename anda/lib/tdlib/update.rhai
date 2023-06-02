if filters.contains("nightly") {
	let ghreq = new_req("https://api.github.com/repos/tdlib/td/commits/HEAD");
	let req = new_req("https://raw.githubusercontent.com/tdlib/td/master/CMakeLists.txt");
	ghreq.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	let sha = json(ghreq.get()).sha;
	rpm.global("commit", sha);
	let v = find("\nproject\\(TDLib\\s+VERSION\\s+([\\d.]+)\\s+", req.get(), 1);
	rpm.global("ver", v);
	rpm.release();
}
