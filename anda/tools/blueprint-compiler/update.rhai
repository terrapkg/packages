let txt = get("https://gitlab.gnome.org/api/v4/projects/17669/releases/");
rpm.version(txt.json_arr()[0].tag_name);
