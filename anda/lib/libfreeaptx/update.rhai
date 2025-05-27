rpm.global("commit", gh_commit("iamthehorker/libfreeaptx"));
if rpm.changed() {
    rpm.release();
    rpm.global("commit_date", date());
    let v = gh_tag("pali/libopenaptx"));
    v.crop(1);
    rpm.global("ver", v);
}
