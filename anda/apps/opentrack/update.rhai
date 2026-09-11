rpm.global("ver", gh("opentrack/opentrack"));
if rpm.changed() {
    rpm.release();
}
