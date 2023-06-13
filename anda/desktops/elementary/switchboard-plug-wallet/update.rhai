let req = new_req("https://api.github.com/repos/elementary/switchboard-plug-wallet/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let sha = json(req.get()).sha;
rpm.version(sha.sub_string(0, 7));
