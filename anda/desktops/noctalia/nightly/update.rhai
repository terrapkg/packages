rpm.global("commit", gh_commit("noctalia-dev/noctalia"));
if rpm.changed() {
        // rpm.global("ver", gh("noctalia-dev/noctalia"));
        rpm.global("commitdate", date());
        rpm.release();
}
