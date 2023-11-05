let sha = get("https://api.github.com/repos/sharanda/manrope/commits/HEAD").json().sha;
if sha != open_file("anda/others/kernel-fyra/commit.txt").read_string() {
	open_file("anda/others/kernel-fyra/commit.txt").write(sha);
	let ver = open_file("anda/others/kernel-fyra/version.txt").parse_int() + 1;
	open_file("anda/others/kernel-fyra/version.txt").write(ver);
}
