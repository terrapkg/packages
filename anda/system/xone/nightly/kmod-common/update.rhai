rpm.global("commit", gh_commit("dlundqvist/xone"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let v = gh("dlundqvist/xone");
    v.crop(1);
    rpm.global("ver", v);
}
