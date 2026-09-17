let stable_tag = `^ensu-v\d+\.\d+\.\d+$`;
let tags = git_tags("https://github.com/ente-io/ente")
  .filter(|tag| stable_tag.find_all(tag).len == 1);
rpm.global("tag", tags[tags.len - 1]);
if rpm.changed() {
  rpm.release();
}
