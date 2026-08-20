let tags = get("https://api.github.com/repos/fluxerapp/fluxer/tags?per_page=100").json_arr();
for tag in tags {
    let v = tag.name;
    if v.starts_with("fluxer-app-proxy@") {
        v.crop(17);
        rpm.version(v);
        break;
    }
}
