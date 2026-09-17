rpm.global("commit", gh_commit("noctalia-dev/umbriel"));
if rpm.changed() {
        // rpm.global("ver", gh("noctalia-dev/umbriel"));
        rpm.global("commitdate", date());
        rpm.release();
}
