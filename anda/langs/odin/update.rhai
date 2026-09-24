rpm.global("ver", gh("odin-lang/Odin"));

if rpm.changed() {
    rpm.release();
}
