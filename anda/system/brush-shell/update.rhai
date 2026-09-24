rpm.global("ver", gh("reubeno/brush"));

if rpm.changed() {
    rpm.release();
}
