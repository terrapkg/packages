rpm.global("commit", gh_commit("morrownr/8821cu-20210916"));
	if rpm.changed() {
		rpm.global("commit_date", date());
		rpm.release();
	}
}
