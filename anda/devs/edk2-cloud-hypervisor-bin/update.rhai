let v = gh_tag("cloud-hypervisor/edk2");
rpm.global("release_tag", v);
v.crop(3);
rpm.global("shortcommit", v);
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
