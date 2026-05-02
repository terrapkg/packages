rpm.global("commit", gh_commit("pop-os/system76-wallpapers"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
