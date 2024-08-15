let v = gitlab_tag("gitlab.freedesktop.org", "176");
if v.contains("-rc") {
  print(`mesa: skipping (rc) ${v}`);
  terminate();
}
v.crop(5);
rpm.global("ver", v);