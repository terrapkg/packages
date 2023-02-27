let txt = get("https://gitlab.gnome.org/api/v4/projects/20662/releases/");
let ver = txt.json_arr()[0].tag_name;
rpm.version(ver);
