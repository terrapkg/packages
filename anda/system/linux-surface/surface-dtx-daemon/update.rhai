rpm.global("ver", gh("linux-surface/surface-dtx-daemon"));

if rpm.changed() {
    rpm.release();
}
