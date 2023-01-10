let req = new_req("https://api.github.com/repos/PrismLauncher/PrismLauncher/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let sha = req.get().json().sha;
rpm.global("commit", sha);
