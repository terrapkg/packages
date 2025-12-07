rpm.global("commit", gh_commit("Sapd/HeadsetControl"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
