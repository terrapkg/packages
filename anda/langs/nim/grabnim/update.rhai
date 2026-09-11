rpm.global("commit", codeberg_commit("janAkali/grabnim"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
