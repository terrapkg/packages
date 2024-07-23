if filters.contains("nightly") {
    rpm.global("commit", gh_commit("neurocyte/flow"));
    if rpm.changed() {
        rpm.release();
        rpm.global("commit_date", date());
    }
}
