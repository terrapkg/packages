rpm.global("commit", gh_commit("noctalia-dev/luciole"));
if rpm.changed() {
    try {
        rpm.global("ver", gh("noctalia-dev/luciole"));
    } catch {}
    rpm.release();
    rpm.global("commitdate", date());
}
