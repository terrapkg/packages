rpm.global("ver", gh_tag("jakcron/nstool"));
if rpm.changed() {
    rpm.release();
}
