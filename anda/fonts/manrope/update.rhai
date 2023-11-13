let readme = get("https://raw.githubusercontent.com/sharanda/manrope/master/README.md");
let ver = find("## Changelog\\n+- v (.+?) \\/", readme, 1);
if ver != find("Version:\\s*([\\d.]+)\n", rpm.f, 1) {
	let req = new_req("https://api.github.com/repos/sharanda/manrope/commits/HEAD");
	let sha = req.get().json().sha;
	rpm.global("commit", sha);
	rpm.version(ver);
}
