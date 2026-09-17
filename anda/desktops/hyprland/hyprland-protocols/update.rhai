rpm.global("commit", gh_commit("hyprwm/hyprland-protocols"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprland-protocols", "main", "VERSION"));
	rpm.global("commit_date", date());
}
