if filters.contains("nightly") {
    rpm.global("commit", gh_commit("OpenGamingCollective/gamescope-session-ogui-steam"));
    if rpm.changed() {
        rpm.release();
        rpm.global("commit_date", date());
    }
}
