rpm.global("commit", gh_commit("Kimplul/hid-tmff2"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let ver = gh("Kimplul/hid-tmff2");
    ver.crop(0);
    rpm.global("ver", ver);

    let tminit = gh_commit("Kimplul/hid-tminit");
    rpm.global("tminit_commit", tminit);
}
