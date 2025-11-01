rpm.global("commit", gh_commit("sched-ext/scx"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let v = gh("sched-ext/scx");
    v.crop(1);
    rpm.global("ver", v);
}
