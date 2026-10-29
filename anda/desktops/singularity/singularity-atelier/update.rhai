rpm.global("commit", gh_commit("singularityos-lab/singularity-atelier"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
