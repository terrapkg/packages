let v = gh("rvaiya/warpd");
try {
	find("(?m)^v[\\d.]+$", v, 0);
	rpm.version(v);
}
catch {}
