rpm.global("ver", gh("arduino/app-bricks-py"));
if rpm.changed() {
    rpm.release();
}
