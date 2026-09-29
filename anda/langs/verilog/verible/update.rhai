let v = gh("https://github.com/chipsalliance/verible");
rpm.global("raw_version", v);
rpm.version("raw_version".replace("-", "~"));
