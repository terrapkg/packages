rpm.global("commit", codeberg_commit("janAkali/grabnim"));
if rpm.changed() {
    rpm.global("commit_date", date());
}
