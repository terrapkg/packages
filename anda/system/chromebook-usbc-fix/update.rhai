if filters.contains("nightly") {
    rpm.global("commit", gh_commit("Ultramarine-Linux/chromebook-usbc-fix"));
    if rpm.changed() {
      rpm.release();
      rpm.global("commit_date", date());
    }
  }
  