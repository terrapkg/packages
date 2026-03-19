rpm.global("commit", get("https://api.github.com/repos/honjow/steamos-manager/commits/dev").json().sha);
if rpm.changed() {
        rpm.global("ver", gh("honjow/steamos-manager"));
        rpm.global("commit_date", date());
        rpm.release();
}
