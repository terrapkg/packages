if filters.contains("nightly") {
  rpm.global("commit", gh_commit("zed-industries/zed"));
  rpm.global("commit_date", date());
  if rpm.changed() {
    let v = find("(\\d+\\.\\d+\\d+\\.\\d+)", find("\nversion = \"(\\d+\\.\\d+\\d+\\.\\d+)\"\n", gh_rawfile("zed-industries/zed", "main", "crates/zed/Cargo.toml"), 1), 1);
    rpm.global("ver", v);
    rpm.global("commit_date", date());
    rpm.release();
  }
}
