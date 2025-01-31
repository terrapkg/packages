let html = get(`https://raw.githubusercontent.com/ghostty-org/ghostty/refs/heads/main/build.zig.zon`);
let ver = find(".version = \"([\\d.]+)\"", html, 1);
rpm.global("commit", gh_commit("ghostty-org/ghostty"));
if rpm.changed() {
    rpm.version(ver);
    rpm.release();
    rpm.global("commit_date", date());
}
