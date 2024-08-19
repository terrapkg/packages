rpm.global("commit", gh_commit("OpenTabletDriver/OpenTabletDriver"));
if rpm.changed() {
    rpm.global("commit_date", date());
    rpm.global("ver", gh("OpenTabletDriver/OpenTabletDriver"));
    rpm.release();
}
