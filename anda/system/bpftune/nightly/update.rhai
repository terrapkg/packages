rpm.global("commit", gh_commit("oracle/bpftune"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("oracle/bpftune");
    rpm.global("ver", v);
}
