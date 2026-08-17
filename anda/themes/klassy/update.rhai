rpm.global("tag", gh("paulmcauley/klassy"));
if rpm.changed() {
  rpm.global("date", date()); // remove if we don't need the `date` macro
  rpm.release();
}
