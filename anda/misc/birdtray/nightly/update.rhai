rpm.global("ver" (gh("gyunaev/birdtray"));
rpm.global("commit", gh_commit("gyunaev/birdtray"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
