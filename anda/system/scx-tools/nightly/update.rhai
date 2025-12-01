rpm.global("commit", gh_commit("sched-ext/scx-loader"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
    let v = gh("sched-ext/scx-loader");
    v.crop(1);
    rpm.global("ver", v);
}
