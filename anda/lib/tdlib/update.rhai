if filters.contains("nightly") {
	let ghreq = new_req("https://api.github.com/repos/tdlib/td/commits/HEAD");
	ghreq.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	rpm.global("commit", json(ghreq.get()).sha);
	let req = new_req("https://raw.githubusercontent.com/tdlib/td/master/CMakeLists.txt");
	let v = find("\nproject\\(TDLib\\s+VERSION\\s+([\\d.]+)\\s+", req.get(), 1);
	rpm.global("ver", v);
	rpm.release();
}
