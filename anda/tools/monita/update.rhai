rpm.global("commit", gh_commit("tau-OS/monita"));
if rpm.changed() {
	rpm.release();
	rpm.global("date", date());
}
