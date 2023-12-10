if filters.contains("nightly") {
	let comp = get("https://raw.githubusercontent.com/nim-lang/Nim/devel/lib/system/compilation.nim");
	let maj = find("\\n\\s*NimMajor.+=\\s*(\\d+)\\n", comp, 1);
	let min = find("\\n\\s*NimMinor.+=\\s*(\\d+)\\n", comp, 1);
	let pat = find("\\n\\s*NimPatch.+=\\s*(\\d+)\\n", comp, 1);
	let v = `${maj}.${min}.${pat}`;
	rpm.global("ver", v);
	let req = new_req("https://api.github.com/repos/nim-lang/Nim/commits/HEAD");
	req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
	rpm.global("commit", req.get().json().sha);
	rpm.release();
}
