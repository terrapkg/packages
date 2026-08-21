rpm.version(gh("isene/glass"));
rpm.global("glyph_ver", gh("isene/glyph"));

if rpm.changed() {
    rpm.release();
}
