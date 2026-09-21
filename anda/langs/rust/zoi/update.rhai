rpm.global("crate_version", crates("zoi-rs"));

if rpm.changed() {
    rpm.release();
}
