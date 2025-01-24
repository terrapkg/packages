rpm.global("commit", gh_commit("intel/ivsc-firmware"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
