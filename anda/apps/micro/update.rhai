if filters.contains("nightly") {
    #rpm.global("commit", gh_commit("zyedidia/micro", "nightly"));
    if rpm.changed() {
        rpm.release();
    }
}  
