rpm.version(gh("isene/glass"));
if rpm.changed() {
    rpm.global("glyph_ver", gh("isene/glyph"));
}
