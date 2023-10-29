let txt = get("https://gitlab.com/api/v4/projects/24742019/repository/tags");
let ver = txt.json_arr()[0].name;
rpm.version(ver);
