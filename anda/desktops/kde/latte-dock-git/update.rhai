let req = new_req("https://api.github.com/repos/KDE/latte-dock/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let _sha = json(req.get()) @ "sha";
let sha = _sha.str();
let cur = find("%global commit (.+)", rpm.f, 1);
if sha != cur {
    rpm.f = sub("%global commit (.+)", `%global commit ${sha}`, rpm.f);
}
