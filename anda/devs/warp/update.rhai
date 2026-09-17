let v = gh_tag("warpdotdev/warp");

if `v[\d.]+\.stable_[\d]+`.find_all(v).len == 1 {
  rpm.version(find(`v([\d.]+)\.stable_[\d]+`, v, 1));
}
