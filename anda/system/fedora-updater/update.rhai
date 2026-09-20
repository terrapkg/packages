rpm.global("commit", gh_commit("rkalla/fedora-updater"));
if rpm.changed() {
  rpm.release();
  rpm.global("commitdate", date());
}
