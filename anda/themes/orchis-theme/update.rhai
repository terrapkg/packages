rpm.global("ver", gh("vinceliuice/Orchis-theme"));

if rpm.changed() {
    rpm.release();
}
