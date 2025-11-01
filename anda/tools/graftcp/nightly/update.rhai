rpm.global("commit", gh_commit("hmgle/graftcp"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
