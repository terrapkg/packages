rpm.global("commit", gh_commit("Fred78290/nct6687d"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
}
