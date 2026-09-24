rpm.global("ver", gh_tag("wailsapp/wails"));
if rpm.changed() {
	rpm.release();
}
