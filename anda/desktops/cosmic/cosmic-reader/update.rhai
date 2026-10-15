rpm.global("commit", gh_commit("pop-os/cosmic-reader"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
