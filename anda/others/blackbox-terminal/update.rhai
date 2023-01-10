let txt = get("https://gitlab.gnome.org/api/v4/projects/20397/releases/");
let ver = txt.json_arr()[0].tag_name;
ver.crop(1);
rpm.version(ver);
