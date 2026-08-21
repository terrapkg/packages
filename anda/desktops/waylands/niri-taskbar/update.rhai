terminate();
rpm.global("crate_version", crates("niri-taskbar"));

if rpm.changed() {
    rpm.release();
}
