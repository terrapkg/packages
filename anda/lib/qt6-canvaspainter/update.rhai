let v = gh_tag("qt/qtcanvaspainter");

if `[\d.]+-beta\d+`.find_all(v).len == 0 && `[\d.]+-rc\d+`.find_all(v).len == 0 {
  rpm.version(v);
}
