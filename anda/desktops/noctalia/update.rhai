let v = gh("noctalia-dev/noctalia");
v.crop(1);

if v >= "5" {
  rpm.global("ver", v);
  v.replace("-", "~");
  rpm.version(v);
}
