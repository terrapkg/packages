if filters.contains("nightly") {
	rpm.global("commit", gitlab_commit("gitlab.gnome.org", "20662", "master"));
	if rpm.changed() {
		let meson = get("https://gitlab.gnome.org/raggesilver/marble/-/raw/master/meson.build");
		rpm.global("ver", find("(?m)^\\s+version:\\s*'(.+)',$", meson, 1));
		rpm.global("commit_date", date());
	}
}
