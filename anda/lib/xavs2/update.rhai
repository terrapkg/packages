rpm.global("commit", gh_commit("pkuvcl/xavs2"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
