rpm.version(gh("kmonad/kmonad"));
if rpm.changed() {
  rpm.release();
}
