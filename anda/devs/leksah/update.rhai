rpm.global("commit", gh_commit("leksah/leksah"));
if rpm.changed() {
    rpm.global("ver", find(`(?m)^version:\s*([\d.]+)`, gh_rawfile("leksah/leksah", "master", "leksah/leksah.cabal"), 1));
    rpm.global("commit_date", date());
    rpm.release();
}
