let repo = "cosmic-utils/cosmic-ext-applet-ollama";
let commit = gh_commit(repo);
rpm.global("commit", commit);

if rpm.changed() {
    let cargo_toml = gh_rawfile(repo, commit, "Cargo.toml");

    rpm.release();
    rpm.global("commitdate", date());
    rpm.global("ver", find(`version = "([\d.]+)"`, cargo_toml, 1));
}
