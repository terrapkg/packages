rpm.global("commit", gh_commit("KyleGospo/bpftune"));
if rpm.changed() {
    # rpm.global("ver", gh("KyleGospo/bpftune"));
    rpm.release();
    rpm.global("commit_date", date());
}