if filters.contains("nightly") {
    rpm.global("commit", gh_commit("OpenGamingCollective/gamescope-session"));
    if rpm.changed() {
        rpm.release();
        rpm.global("commit_date", date());
    }
}
