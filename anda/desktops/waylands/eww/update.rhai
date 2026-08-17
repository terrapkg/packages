rpm.global("commit", gh_commit("elkowar/eww"));
if rpm.changed() {
    rpm.global("ver", gh("elkowar/eww"));
    rpm.global("commit_date", date());
    rpm.release();
}
