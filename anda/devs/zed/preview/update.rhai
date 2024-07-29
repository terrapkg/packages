let releases = "https://api.github.com/repos/zed-industries/zed/releases".get().json_arr();
for release in releases {
  let tag = release.tag_name;
  tag.pop(4); // remove the "-pre" suffix
  tag.crop(1); // remove "v"
  rpm.global("ver", tag);
  break;
  if rpm.changed() {
    rpm.release();
  }
}
