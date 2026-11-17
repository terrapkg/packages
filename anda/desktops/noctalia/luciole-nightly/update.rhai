rpm.global("commit", gh_commit("noctalia-dev/luciole"));
if (rpm.changed()) {
    // rpm.global("version", gh("noctalia-dev/luciole"));
    rpm.release();
    rpm.global("commitdate", date())
}
