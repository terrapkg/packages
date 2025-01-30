if filters.contains("nightly") {
    rpm.global("commit", gh_commit("dqrk0jeste/owl"));
    if rpm.changed() {
        rpm.global("commit_date", date());
    }
}
