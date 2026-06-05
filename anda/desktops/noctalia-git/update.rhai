rpm.global("commit", get("https://api.github.com/repos/noctalia-dev/noctalia-shell/commits/v5").json().sha);
if rpm.changed() {
        // rpm.global("ver", gh("noctalia-dev/noctalia-shell"));
        rpm.global("commit_date", date());
        rpm.release();
}
