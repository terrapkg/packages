rpm.global("commit", gh_commit("PikaOS-Linux/falcond-profiles"));
	if rpm.changed() {
		rpm.global("commit_date", date());
		rpm.release();
	}
}
