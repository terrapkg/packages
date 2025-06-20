rpm.global("commit", gh_commit("intel/usbio-drivers"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
