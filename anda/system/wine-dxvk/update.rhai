rpm.version(gh("doitsujin/dxvk"));
if rpm.changed {
    let json = get("https://api.github.com/repos/doitsujin/dxvk/contents/subprojects").json_arr();
    rpm.global("libdisplay_commit", json[0].sha);
    let rawfile = get("https://gitlab.freedesktop.org/emersion/libdisplay-info/-/raw/main/meson.build?ref_type=heads");
    let v = find("version: '([\\d.]+....)'", rawfile, 1);
    rpm.global("libdisplay_ver", v);
}
