rpm.global("commit", gh_commit("singularityos-lab/singularity-accounts"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
