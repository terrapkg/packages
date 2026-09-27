rpm.global("commit", gh_commit("noctalia-dev/noctalia"));
if rpm.changed() {
    let v = gh("noctalia-dev/noctalia");
    v.replace("-", "~");
    rpm.global("ver", v.crop(1));
    rpm.global("commitdate", date());
    rpm.release();
}
