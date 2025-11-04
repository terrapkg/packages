rpm.global("commit", gh_commit("denilsonsa/udev-joystick-blacklist"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
