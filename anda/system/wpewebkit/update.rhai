// Stable WPE WebKit releases have an even minor version (odd = development)
let latest = "";
let best = 0;
for m in find_all(`wpewebkit-(\d+)\.(\d+)\.(\d+)\.tar\.xz`, get("https://wpewebkit.org/releases/")) {
	let minor = m[2].parse_int();
	if minor % 2 != 0 { continue; }
	let key = m[1].parse_int() * 1000000 + minor * 1000 + m[3].parse_int();
	if key > best {
		best = key;
		latest = `${m[1]}.${minor}.${m[3]}`;
	}
}
rpm.version(latest);
