rpm.global("ver", gh("veracrypt/VeraCrypt"));

if rpm.changed() {
    rpm.release();
}
