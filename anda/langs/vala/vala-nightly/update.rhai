if filters.contains("nightly") {
	let req = new_req("https://gitlab.gnome.org/api/v4/projects/1551/repository/branches/main");
	let sha = json(req.get()).commit.id;
	rpm.global("commit", sha);
	rpm.release();
}
