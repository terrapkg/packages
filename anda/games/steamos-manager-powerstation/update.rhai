rpm.global("commit", get("https://api.github.com/repos/OpenGamingCollective/steamos-manager/commits/dev").json().sha);
if rpm.changed() {
        rpm.global("commit_date", date());
        rpm.release();
}
