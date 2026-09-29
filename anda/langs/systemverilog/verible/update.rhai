let v = gh("https://github.com/chipsalliance/verible");
rpm.global("raw_version", v);
v.replace("-", "~")
rpm.version(v);
