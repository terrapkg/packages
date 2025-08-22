let v = gh_tag("fraunhoferhhi/vvenc");
if `[\d.]+-rc\d+`.find_all(v).len == 0 {
  rpm.version(v);
}
