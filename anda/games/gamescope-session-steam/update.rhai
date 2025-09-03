if filters.contains("nightly") {
    rpm.global("commit", gh_commit("bazzite-org/gamescope-session-steam"));
    if rpm.changed() {
        rpm.release();
        rpm.global("commit_date", date());
    }
}
