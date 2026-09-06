rpm.global("commit", gh_commit("singularityos-lab/vetro"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
