rpm.global("commit", gh_commit("cloud-hypervisor/cloud-hypervisor"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
