let v = gh("openzfs/zfs");
if v.starts_with("zfs-") {
    v.crop(4);
    rpm.version(v);
}
