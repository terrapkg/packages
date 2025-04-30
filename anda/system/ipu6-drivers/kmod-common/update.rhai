rpm.global("ipu6_commit", gh_commit("intel/ipu6-drivers"));
if rpm.changed() {
    rpm.release();
    rpm.global("usbio_commit", gh_commit("intel/usbio-drivers"));
    rpm.global("ipu6_commitdate", date());
}
