rpm.global("commit", gh_commit("scarburato/t150_driver"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    rpm.global("ver", gh("scarburato/t150_driver"));
}
