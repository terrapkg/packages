rpm.global("commit", gh_commit("pondda/tmon"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}

