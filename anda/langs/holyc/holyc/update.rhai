let v = gh("Jamesbarford/holyc-lang");
v.crop(1);
rpm.global("ver", v);
if v.ends_with("-release") {
  v.pop(8);
}
v.replace("-", "~");
rpm.version(v);
