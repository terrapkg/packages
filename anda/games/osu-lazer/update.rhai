let v = gh("ppy/osu");
if v.ends_with("-lazer") {
    v.pop(6);
    rpm.version(v);
    if rpm.changed() {
        rpm.define("osuresver", gh("ppy/osu-resources"));
    }
}
