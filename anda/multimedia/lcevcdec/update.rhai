rpm.version(gh("v-novaltd/LCEVCdec"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit", gh_commit("v-novaltd/LCEVCdec"));
    rpm.global("commit_date", date());
}
