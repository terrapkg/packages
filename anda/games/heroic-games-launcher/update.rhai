let v = gh("Heroic-Games-Launcher/HeroicGamesLauncher");
// Store for later
let vv = v;
v.crop(1);
rpm.version(v);
// Versions for bundled binaries. Most important for Legendary as Fedora packages this.
if rpm.changed() {
    let html = gh_rawfile("Heroic-Games-Launcher/HeroicGamesLauncher", vv, "meta/downloadHelperBinaries.ts");
    let lv = find("legendary: '([\\d.]+)'", html, 1);
    let gv = find("gogdl: 'v([\\d.]+)'", html, 1);
    let nv = find("nile: 'v([\\d.]+)'", html, 1);
    let cv = find("comet: 'v([\\d.]+)'", html, 1);
    rpm.global("legendary_version", lv);
    rpm.global("gogdl_version", gv);
    rpm.global("nile_version", nv);
    rpm.global("comet_version", cv);
}
