rpm.global("commit", gh_commit("chocolateimage/fontviewer"));
if rpm.changed() {
	rpm.release();
}