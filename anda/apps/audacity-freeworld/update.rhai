rpm.global("ver", gh("audacity/audacity"));
if rpm.changed() {
    rpm.release();
}
