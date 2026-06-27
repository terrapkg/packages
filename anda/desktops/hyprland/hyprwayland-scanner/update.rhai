rpm.global("commit", gh_commit("hyprwm/hyprwayland-scanner"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprwayland-scanner", "main", "VERSION"));
	rpm.global("commit_date", date());
}
