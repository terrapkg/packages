let v = gh("rvaiya/warpd");
if find("(?m)^v[\\d.]+$", v, 0) {
	rpm.version(v);
}
