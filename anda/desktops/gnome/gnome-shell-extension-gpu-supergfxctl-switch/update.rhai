if filters.contains("nightly") {
  rpm.global("commit", gh_commit("chikobara/GPU-Switcher-Supergfxctl"));
  if rpm.changed() {
    let v = find("\"version\": ([.\\d]+)\n", gh_rawfile("chikobara/GPU-Switcher-Supergfxctl", "main", "metadata.json"), 1);
    rpm.global("ver", v);
    rpm.global("commit_date", date());
    rpm.release();
  }
}
