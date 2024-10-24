rpm.global("commit", gh_commit("OpenTabletDriver/OpenTabletDriver"));
if rpm.changed() {
    rpm.global("commit_date", date());
    let v = gh("OpenTabletDriver/OpenTabletDriver");
    v.crop(1); // "v" prefix
    rpm.global("ver", v);
    rpm.release();
}
