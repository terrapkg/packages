let v = gh_tag("fraunhoferhhi/vvdec");
if `[\d.]+-rc\d+`.find_all(v).len == 0 {
  rpm.version(v);
}
