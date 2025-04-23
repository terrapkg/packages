let url = `https://api.github.com/repos/ghostty-org/ghostty/releases/83450291`;
let json = get(url).json();
let commit = json.target_commitish;
rpm.global("commit", commit);
if rpm.changed() {
    let date = json.created_at;
    date.truncate(10);
    let html = get(`https://raw.githubusercontent.com/ghostty-org/ghostty/refs/heads/main/build.zig.zon`);
    let ver = find(".version = \"([\\d.]+)\"", html, 1);
    rpm.global("fulldate", date);
    rpm.global("ver", ver);
    rpm.release();
}
