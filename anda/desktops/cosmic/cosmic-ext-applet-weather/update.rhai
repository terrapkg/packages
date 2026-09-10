rpm.global("commit", gh_commit("cosmic-utils/cosmic-ext-applet-weather"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
