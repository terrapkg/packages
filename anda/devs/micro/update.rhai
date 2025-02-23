rpm.global("commit", gh_commit("zyedidia/micro"));
if rpm.changed() {
	rpm.global("commit_date", date());
}
