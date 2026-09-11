let v = gh("linux-surface/surface-control");
rpm.global("ver", v);
v.crop(1);
v.replace("-", ".");
rpm.version(v);
