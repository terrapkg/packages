let v = gh("Jamesbarford/holyc-lang");
v.crop(1);
rpm.global("ver", v);
v.replace("-", "~");
rpm.version(v);
