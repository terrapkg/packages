let releases = "https://api.github.com/repos/ruffle-rs/ruffle/releases".get().json_arr();
for release in releases {
  let tag = release.tag_name;
  if !tag.starts_with("nightly-") {
    continue;
  }
  tag.crop(8); // remove "nightly-"
  rpm.global("ver", tag);
  break;
}
if rpm.changed() {
  rpm.release();
}
