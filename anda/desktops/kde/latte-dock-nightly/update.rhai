let req = new_req("https://api.github.com/repos/KDE/latte-dock/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let sha = json(req.get()).sha;
rpm.global("commit", sha);
