let txt = get("https://gitlab.gnome.org/api/v4/projects/20397/releases/");
let ver = json(txt).get_json(0).get_json("tag_name").string_json()[1:];
rpm.version(ver);
