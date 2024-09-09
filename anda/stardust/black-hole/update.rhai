if filters.contains("nightly") {
    rpm.global("commit", gh_commit("StardustXR/black-hole"));
    if rpm.changed() {
      rpm.release();
      rpm.global("commit_date", date());
    }
  }
}