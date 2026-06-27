rpm.global("commit", gh_commit("games-on-whales/inputtino"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
