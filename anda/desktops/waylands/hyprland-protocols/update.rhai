rpm.global("commit", gh_commit("hyprwm/hyprlang-protocols"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprlang-protocols", "main", "VERSION"));
	rpm.global("commit_date", date());
}
