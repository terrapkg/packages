let ver = gh("gyunaev/birdtray");
ver.crop(1);
rpm.global("ver", ver);
rpm.global("commit", gh_commit("gyunaev/birdtray"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
