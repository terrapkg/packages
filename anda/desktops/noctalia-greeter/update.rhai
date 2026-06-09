rpm.global("commit", get("https://api.github.com/repos/noctalia-dev/noctalia-greeter/commits/main").json().sha);
if rpm.changed() {
        rpm.global("ver", gh("noctalia-dev/noctalia-greeter"));
        rpm.global("commit_date", date());
        rpm.release();
}
