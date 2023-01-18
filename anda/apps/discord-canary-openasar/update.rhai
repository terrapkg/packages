let req = new_req("https://api.github.com/repos/GooseMod/OpenAsar/commits/HEAD");
req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
let _sha = json(req.get()) @ "sha";
let sha = _sha.str();
let cur = find("%define commit (.+)", rpm.f, 1);
if sha != cur {
    print(`openasar-canary: ${cur} -> ${sha}`);
    rpm.f = sub("%define commit (.+)", `%define commit ${sha}`, rpm.f);
} else {
    print("openasar-canary: Up to date!");
}
let html = get("https://discordapp.com/api/download/canary?platform=linux&format=tar.gz");
let newver = find("https://dl-canary\\.discordapp\\.net/apps/linux/([\\.\\d]+)/", html, 1);
rpm.version(newver);
