let v = gh_rawfile("Heroic-Games-Launcher/HeroicGamesLauncher", "main", "package.json").json()["version"];
rpm.version(v);
// Versions for bundled binaries. Most important for Legendary as Fedora packages this.
if rpm.changed() {
    let ts = gh_rawfile("Heroic-Games-Launcher/HeroicGamesLauncher", `v${v}`, "meta/downloadHelperBinaries.ts");
    let lv = find("legendary: '([\\d.]+)'", ts, 1);
    let gv = find("gogdl: 'v([\\d.]+)'", ts, 1);
    let nv = find("nile: 'v([\\d.]+)'", ts, 1);
    let cv = find("comet: 'v([\\d.]+)'", ts, 1);
    rpm.global("legendary_version", lv);
    rpm.global("gogdl_version", gv);
    rpm.global("nile_version", nv);
    rpm.global("comet_version", cv);
}
