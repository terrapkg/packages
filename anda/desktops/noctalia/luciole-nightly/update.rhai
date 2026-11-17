rpm.global("commit", gh_commit("noctalia-dev/luciole"));
if (rpm.changed()) {
    rpm.release();
    rpm.global("date", date())
}
