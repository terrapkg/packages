rpm.global("ver", gh("vercel/geist-font"));
if rpm.changed() {
    rpm.release();
}
