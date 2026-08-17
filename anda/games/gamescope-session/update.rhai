if filters.contains("nightly") {
    rpm.global("commit", gh_commit("ChimeraOS/gamescope-session"));
    if rpm.changed() {
        rpm.release();
        rpm.global("commit_date", date());
    }
}
