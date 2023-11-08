let ver = gh("graalvm/graalvm-ce-builds");
if ver.starts_with("vm-") {
	ver.crop(3);
	rpm.version(ver);
} else if ver.starts_with("graal-") {
	ver.crop(6);
	rpm.version(ver);
} else {
	print(`graalvm: ${ver}?`);
}
