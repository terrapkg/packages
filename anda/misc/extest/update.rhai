rpm.global("commit", gh_commit("bazzite-org/extest"));
if rpm.changed() {
	rpm.global("commit_date", date());
	rpm.release();
}
