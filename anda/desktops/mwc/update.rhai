if filters.contains("nightly") {
    rpm.global("commit", gh_commit("dqrk0jeste/mwc"));
    let v = gh("dqrk0jeste/mwc");
    if rpm.changed() {
        rpm.global("commit_date", date());
        v.crop(1);
        rpm.global("ver", v);
    }
}
