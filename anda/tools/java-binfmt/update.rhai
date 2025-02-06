rpm.global("commit", gh_commit("terrapkg/pkg-java-binfmt"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
}
