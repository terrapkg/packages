rpm.global("ver", gh("AppImageCommunity/zsync2"));
if rpm.changed() {
  rpm.global("git_commit", gh_commit("AppImageCommunity/zsync2"));
}
