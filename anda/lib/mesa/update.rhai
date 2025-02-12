let v = gitlab_tag("gitlab.freedesktop.org", "176");
v.crop(5);
if `[\d.]+-rc\d+`.find_all(v).len == 0 {
  rpm.version(v);
}
