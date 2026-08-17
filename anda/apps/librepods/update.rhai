let tag = gh("kavishdevar/librepods");
if `[\d.]+-alpha.*`.find_all(tag).len == 0 && `[\d.]+-rc\.\d+`.find_all(tag).len == 0 && `nightly-.*`.find_all(tag).len == 0 {
  if tag.ends_with("-hotfix") {
    tag.crop(7);
  }
  rpm.version(tag);
}
