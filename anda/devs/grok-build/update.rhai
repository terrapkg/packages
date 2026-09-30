rpm.global("commit", gh_commit("xai-org/grok-build"));
if rpm.changed() {
    let v = find("\nversion = \"([.\\d]+)\"\n", gh_rawfile("xai-org/grok-build", "main", "crates/codegen/xai-grok-pager-bin/Cargo.toml"), 1);
    rpm.global("ver", v);
    rpm.global("commit_date", date());
    rpm.release();
}
