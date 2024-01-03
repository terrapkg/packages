let tags = get("https://api.github.com/repos/AyatanaIndicators/ayatana-indicator-session/git/refs/tags").json_arr();
let split_ref = tags[tags.len-1].ref.split("/");
rpm.version(split_ref[split_ref.len-1]);
