rpm.global("commit", gh_commit("intel/ipu6-camera-hal"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh("intel/ipu6-camera-hal");
    v.truncate(6);
    v.crop(1);
    rpm.global("ver", v);
}
