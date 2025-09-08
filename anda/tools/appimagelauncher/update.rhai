let v = gh("TheAssassin/AppImageLauncher");
if v.starts_with("v") {
	v.crop(1);
}
rpm.globall("ver", v);
