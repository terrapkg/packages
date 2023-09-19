let sha = get("https://api.github.com/repos/sharanda/manrope/commits/HEAD").json().sha;
if sha != open_file("commit.txt").read_string() {
	open_file("commit.txt").write(sha);
	let ver = open_file("version.txt").parse_int() + 1;
	open_file("version.txt").write(ver);
}
