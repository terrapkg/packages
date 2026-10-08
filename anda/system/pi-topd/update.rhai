let v = gh("pi-top/pi-topd");
v.crop(1);
rpm.global("ver", v);

if rpm.changed() {
    rpm.release();
}
