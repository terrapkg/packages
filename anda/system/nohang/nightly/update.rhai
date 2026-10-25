rpm.global("commit", gh_commit("hakavlad/nohang"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let version = gh("hakavlad/nohang");
    version.crop(1);
    rpm.global("ver", version);
}
