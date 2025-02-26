rpm.global("commit_hash", gh_commit("zyedidia/micro"));
let v = gh("zyedidia/micro");
if rpm.changed() {
    rpm.global("commit_date", date());
    rpm.global("ver", v.crop(1));
}
