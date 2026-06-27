rpm.global("commit", gh_commit("BoukeHaarsma23/zenergy"));
if rpm.changed() {
    rpm.release();
    rpm.global("commitdate", date());
}
