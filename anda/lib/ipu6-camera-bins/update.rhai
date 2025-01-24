rpm.global("commit", gh_commit("intel/ipu6-camera-bins"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
