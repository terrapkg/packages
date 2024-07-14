if filters.contains("nightly") {
  rpm.global("commit", gh_commit("zed-industries/zed"));
  if rpm.changed() {
    let v = find("\nversion = \"([.\\d]+)\"\n", gh_rawfile("zed-industries/zed", "main", "crates/zed/Cargo.toml"), 1);
    rpm.global("ver", v);
    rpm.global("commit_date", date());
    rpm.release();
  }
}
