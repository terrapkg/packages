rpm.global("commit", gh_commit("Ebbo/cosmic-applet-package-updater"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
