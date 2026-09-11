rpm.global("upstream_ver", gh("subframe7536/Maple-font"));
if rpm.changed() {
    rpm.release();
}
