let tags = json_arr(get("https://api.github.com/repos/kavishdevar/librepods/tags"));
print(tags);
tag = tags.filter(|t| t.starts_with("linux-"));
print(tag);
rpm.version(tag.remove("linux-"))
