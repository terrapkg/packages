let r = get("https://api.github.com/repos/ghostty-org/ghostty/releases/83450291").json();
rpm.global("commit", r.target_commitish);
if rpm.changed() {
    let d = sh(`date -d "${r.created_at}" "+%Y%m%d%H%M"`, #{"stdout": "piped"}).ctx.stdout;
    d.pop()
    rpm.version(d);
    let z = get(`https://raw.githubusercontent.com/ghostty-org/ghostty/refs/heads/main/build.zig.zon`);
    let v = find("\\.version = \"([\\d.]+)-dev\"", z, 1);
    rpm.global("ver", v);
}
