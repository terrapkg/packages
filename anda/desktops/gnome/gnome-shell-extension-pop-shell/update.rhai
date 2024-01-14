if filters.contains("nightly") {
  rpm.global("commit", get("https://api.github.com/repos/pop-os/shell/commits/HEAD").json().sha);
  rpm.global("ver", gh("pop-os/shell"));
}
