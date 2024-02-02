let txt = get("https://gitlab.com/api/v4/projects/52322952/repository/tags");
fn get_ver(json) {
    for release in json {
        if "unl0kr" in release.name {
            return release.name.split("-")[1]
        }
    }
}
let ver = get_ver(txt.json_arr());
rpm.version(ver);
