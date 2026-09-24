rpm.global("ver", gh("oracle/bpftune"));

if rpm.changed() {
    rpm.release();
}
