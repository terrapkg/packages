rpm.global("commit", gh_commit("noctalia-dev/xdg-desktop-portal-umbriel"));
if rpm.changed() {
        // rpm.global("ver", gh("noctalia-dev/xdg-desktop-portal-umbriel"));
        rpm.global("commitdate", date());
        rpm.release();
}
