rpm.global("ver", gh("Boof2015/astra"));
if rpm.changed() {
    rpm.release();
}
