let latest = "";
let best = 0;
for m in find_all(`wpebackend-fdo-(\d+)\.(\d+)\.(\d+)\.tar\.xz`, get("https://wpewebkit.org/releases/")) {
	let key = m[1].parse_int() * 1000000 + m[2].parse_int() * 1000 + m[3].parse_int();
	if key > best {
		best = key;
		latest = `${m[1]}.${m[2]}.${m[3]}`;
	}
}
rpm.version(latest);