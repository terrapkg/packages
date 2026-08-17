let tag = gh("kavishdevar/librepods");
if `[\d.]+-alpha.*`.find_all(tag).len == 0 && `[\d.]+-rc.*`.find_all(tag).len == 0 && `nightly-.*`.find_all(tag).len == 0 {
  rpm.global("ver", tag);
}

if rpm.changed() {
  rpm.release();
}
