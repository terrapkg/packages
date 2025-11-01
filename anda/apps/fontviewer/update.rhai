rpm.version(gh("chocolateimage/fontviewer"));
if rpm.changed() {
  rpm.release();
}
