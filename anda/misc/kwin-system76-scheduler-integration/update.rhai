rpm.global("commit", gh("maxiberta/kwin-system76-scheduler-integration"));
if rpm.changed() {
  rpm.global("date", date()); // remove if we don't need the `date` macro
  rpm.release();
}
