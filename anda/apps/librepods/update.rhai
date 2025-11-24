let tags = json_arr(get("https://api.github.com/repos/kavishdevar/librepods/tags"));
let tag = tags.find(|t| t.name.starts_with("linux-v"));
tag.name.crop(7);
rpm.version(tag.name);
