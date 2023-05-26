if filters.contains("nightly") {
	// let txt = get("https://gitlab.gnome.org/api/v4/projects/14079/repository/tags?per_page=1");
	// let ver = txt.json_arr()[0].name;
	// rpm.global("ver", ver);
	txt = get("https://gitlab.gnome.org/api/v4/projects/14079/repository/commits?per_page=1&page=1");
	let commit = txt.json_arr()[0].id;
	rpm.global("commit", commit);
}
