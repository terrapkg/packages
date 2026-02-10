let v = gh("Jamesbarford/holyc-lang");
v.crop(6);
rpm.global("ver", v);

if rpm.changed() {
  rpm.release()
}
