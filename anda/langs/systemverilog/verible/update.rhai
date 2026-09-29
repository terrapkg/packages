let v = gh("chipsalliance/verible");
rpm.global("raw_version", v);
v.replace("-", "~")
rpm.version(v);
