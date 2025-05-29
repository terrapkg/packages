rpm.global("commit", gh_commit("morrownr/8821cu-20210916"));
	if rpm.changed() {
		rpm.global("commit_date", date());
		rpm.release();
                let v = find(`PACKAGE_VERSION="([\d.]+)"`, gh_rawfile("morrownr/8821cu-20210916", "main", "dkms.conf"), 1);
                rpm.global("ver", v);
	}
}
