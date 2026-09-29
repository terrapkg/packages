rpm.global("ver", gh("SagerNet/sing-box"));
if rpm.changed() {
    rpm.release();
}
