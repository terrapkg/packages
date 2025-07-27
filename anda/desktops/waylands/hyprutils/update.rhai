rpm.global("commit", gh_commit("hyprwm/hyprutils"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprutils", "main", "VERSION"));
	rpm.global("commit_date", date());
}
