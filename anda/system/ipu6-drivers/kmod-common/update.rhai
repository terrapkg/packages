rpm.global("commit", gh_commit("intel/ipu6-drivers"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
