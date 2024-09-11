rpm.global("commit", gh_commit("StardustXR/protostart"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
