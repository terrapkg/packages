rpm.global("tag", gh("wineasio/wineasio"))

if rpm.changed() {
    rpm.release();
}
