rpm.global("commit", gh_commit("singularityos-lab/libsingularity"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
