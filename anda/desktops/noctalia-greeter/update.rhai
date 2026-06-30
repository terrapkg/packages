rpm.global("commit", gh_commit("noctalia-dev/noctalia-greeter"));
if rpm.changed() {
        rpm.global("ver", gh("noctalia-dev/noctalia-greeter"));
        rpm.global("commit_date", date());
        rpm.release();
}
