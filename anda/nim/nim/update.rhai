let req = new_req("https://api.github.com/repos/nim-lang/Nim/tags");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let ver = req.get().json_arr()[0].name;
ver.crop(1);
rpm.version(ver);
