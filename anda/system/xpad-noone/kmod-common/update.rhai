rpm.global("commit", gh_commit("medusalix/xpad-noone"));
if rpm.changed() {
    rpm.release();
    rpm.global("date", date());
}
