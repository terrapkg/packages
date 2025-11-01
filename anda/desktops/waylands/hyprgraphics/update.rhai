rpm.global("commit", gh_commit("hyprwm/hyprgraphics"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprgraphics", "main", "VERSION"));
	rpm.global("commit_date", date());
}
