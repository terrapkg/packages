rpm.global("ver", gh("adobe-fonts/source-han-serif"));
if rpm.changed() {
    rpm.release();
}
