let version = gh("mescon/logitech-trueforce-linux-driver");
if version.starts_with("v") {
	version.crop(1);
}
rpm.global("repoversion", version);
