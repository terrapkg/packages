if filters.contains("nightly") {
	rpm.global("commit", gh_commit("nim-lang/Nim"));
	if rpm.changed() {
		let comp = get("https://raw.githubusercontent.com/nim-lang/Nim/devel/lib/system/compilation.nim");
		let maj = find("\\n\\s*NimMajor.+=\\s*(\\d+)\\n", comp, 1);
		let min = find("\\n\\s*NimMinor.+=\\s*(\\d+)\\n", comp, 1);
		let pat = find("\\n\\s*NimPatch.+=\\s*(\\d+)\\n", comp, 1);
		let v = `${maj}.${min}.${pat}`;
		rpm.global("ver", v);
		rpm.release();
		rpm.global("commit_date", date());
	}
}
