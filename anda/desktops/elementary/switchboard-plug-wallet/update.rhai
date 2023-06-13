let req = new_req("https://api.github.com/repos/elementary/switchboard-plug-wallet/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
rpm.global("commit", json(req.get()).sha);
