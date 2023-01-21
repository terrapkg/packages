let req = new_req("https://api.github.com/repos/vala-lang/vala-language-server/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let _sha = json(req.get()) @ "sha";
let sha = _sha.str();
let cur = find("%global commit (.+)", rpm.f, 1);
if sha != cur {
    print(`vala-language-server-nightly: ${cur} -> ${sha}`);
    rpm.f = sub("%global commit (.+)", `%global commit ${sha}`, rpm.f);
} else {
    print("vala-language-server-nightly: Up to date!");
}
