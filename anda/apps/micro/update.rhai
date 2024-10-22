if filters.contains("nightly") {
    rpm.global("commit", gh_commit("zyedidia/micro"));
    if rpm.changed() {
        rpm.release();
    }
}  
