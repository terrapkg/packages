rpm.global("commit", gh_commit("AdisonCavani/distro-grub-themes"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
