rpm.global("commit", gh_commit("iamthehorker/libfreeaptx"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    rpm.global("ver", gh_tag("pali/libopenaptx"));
}
