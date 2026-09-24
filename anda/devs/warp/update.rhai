let tags = git_tags("https://github.com/warpdotdev/warp");
tags.reverse();

for tag in tags {
  if `v[\d.]+\.stable_[\d]+`.find_all(tag).len == 1 {
    rpm.version(find(`v([\d.]+)\.stable_[\d]+`, tag, 1));
    break;
  }
}
