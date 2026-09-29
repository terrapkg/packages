let v = gh("chipsalliance/verible");
v.crop(1);
rpm.global("raw_version", v);
v.replace("-", "~");
rpm.version(v);
