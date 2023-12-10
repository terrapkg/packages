let release = get("https://api.github.com/repos/vscodium/vscodium/releases").json_arr()[0];
let i = 0;
for asset in release.assets {
	if asset.name == `VSCodium-linux-x64-${release.tag_name}.tar.gz` || asset.name == `VSCodium-linux-arm64-${release.tag_name}.tar.gz` {
		i += 1;
	}
}
if i == 2 {
	rpm.version(release.tag_name);
}
