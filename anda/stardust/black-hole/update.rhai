if filters.contains("nightly") {
    rpm.global("commit", gh_commit("StardustXR/server"));
    if rpm.changed() {
      rpm.release();
      rpm.global("commit_date", date());
    }
  }
}
