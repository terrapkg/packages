rpm.global("ver", gh("KyleGospo/bpftune"));
rpm.global("commit", gh_commit("KyleGospo/bpftune"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}