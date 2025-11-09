rpm.global("commit", gh_commit("hyprwm/hyprlang"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprlang", "main", "VERSION"));
	rpm.global("commit_date", date());
}
