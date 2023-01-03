let req = new_req("https://api.github.com/repos/PrismLauncher/PrismLauncher/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let _sha = json(req.get()) @ "sha";
let sha = _sha.str();
let cur = find("%global commit (.+)", rpm.f, 1);
if sha != cur {
    print(`prismlauncher-nightly: ${cur} -> ${sha}`);
    rpm.f = sub("%global commit (.+)", `%global commit ${sha}`, rpm.f);
} else {
    print("prismlauncher-nightly: Up to date!");
}