let latest_tag = get("https://codeberg.org/api/v1/repos/valos/Komikku/tags").json_arr()[0].name;
let new_version = find("([\\.\\d]+)", latest_tag, 1);
rpm.global("raw_ver", latest_tag);
rpm.version(new_version);
