rpm.global("commit", gh_commit("falkTX/Carla"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("falkTX/Carla");
    v.crop(1);
    rpm.global("ver", v);
}
