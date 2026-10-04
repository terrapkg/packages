// /releases/latest skips draft and prerelease tags, including the weekly builds.
let release = get("https://api.github.com/repos/FreeCAD/FreeCAD/releases/latest").json();
rpm.version(release.tag_name);
if rpm.changed() {
    rpm.release();
}
