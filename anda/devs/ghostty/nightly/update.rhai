rpm.global("commit", gh_commit("ghostty-org/ghostty"));
if rpm.changed() {
    let html = get(`https://raw.githubusercontent.com/ghostty-org/ghostty/refs/heads/main/build.zig.zon`);
    let ver = find(".version = \"([\\d.]+)\"", html, 1);
    rpm.version(gh_tag("ghostty-org/ghostty"));
    rpm.release();
    rpm.global("dev_ver", ver);
    rpm.global("commit_date", date());
}
