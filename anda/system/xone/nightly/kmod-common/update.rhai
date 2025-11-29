rpm.global("commit", gh_commit("dlundqvist/xone"));
if rpm.changed() {
    import "andax/bump_extras.rhai" as bump;
    rpm.release();
    rpm.global("commitdate", date());
    let ver = bump::madoguchi("xone", labels.branch);
    ver.crop(1);
    rpm.global("ver", ver);
}
