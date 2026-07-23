rpm.global("commit", gh_commit("scarburato/t150_driver"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let ver = gh("scarburato/t150_driver");
    ver.crop(0);
    rpm.global("ver", ver);
}
