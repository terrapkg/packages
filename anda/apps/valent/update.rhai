if filters.contains("nightly") {
    rpm.global("commit", gh_commit("andyholmes/valent"));
    if rpm.changed() {
        rpm.release();
        rpm.global("commit_date", date());
    }
}
