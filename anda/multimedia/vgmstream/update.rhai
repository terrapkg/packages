rpm.global("commit", gh_commit("vgmstream/vgmstream"));
if rpm.changed() {
	rpm.global("commit_date", date());
	rpm.release();
}
