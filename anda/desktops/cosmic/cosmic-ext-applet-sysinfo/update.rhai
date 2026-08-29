let repo = "cosmic-utils/cosmic-ext-applet-sysinfo";
let commit = gh_commit(repo);
rpm.global("commit", commit);

if rpm.changed() {
    let cargo_toml = gh_rawfile(repo, commit, "Cargo.toml");

    rpm.release();
    rpm.global("commit_date", date());
    rpm.global("ver", find(`version = "([\d.]+)"`, cargo_toml, 1));
}
