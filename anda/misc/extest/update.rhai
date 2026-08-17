rpm.global("commit", gh_commit("KyleGospo/extest"));
if rpm.changed() {
	rpm.global("commit_date", date());
	rpm.release();
}