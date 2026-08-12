rpm.global("commit_hash", gh_commit("micro-editor/micro"));
if rpm.changed() {
    rpm.global("commit_date", date());
    let v = gh("micro-editor/micro");
    v.crop(1);
    rpm.global("ver", v);
}
