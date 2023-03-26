let txt = get("https://gitlab.com/api/v4/projects/17117115/repository/tags");
rpm.version(txt.json_arr()[0].name);
