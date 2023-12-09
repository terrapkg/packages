let sha = get("https://api.github.com/repos/ellyq/linux/commits/HEAD").json().sha;
if sha != open_file("anda/system/kernel-mt8183/commit.txt").read_string() {
	open_file("anda/system/kernel-mt8183/commit.txt").write(sha);
	let ver = open_file("anda/system/kernel-mt8183/version.txt").parse_int() + 1;
	open_file("anda/system/kernel-mt8183/version.txt").write(ver);
}
