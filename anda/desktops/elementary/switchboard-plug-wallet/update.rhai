rpm.global("commit", gh_commit("elementary/switchboard-plug-wallet"));
if rpm.changed() {
	rpm.global("commit_date", date());
}
