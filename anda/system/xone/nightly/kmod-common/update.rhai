import "andax/bump_extras.rhai" as bump;

rpm.global("commit", gh_commit("dlundqvist/xone"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    rpm.global("ver", bump::madoguchi("xone", labels.branch));
}
