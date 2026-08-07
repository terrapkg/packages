rpm.global("commit", gh_commit("amkillam/ryzen_smu"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
}
