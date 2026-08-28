let tags = git_tags("https://github.com/ente-io/ente");
for tag in tags {
  if tag.starts_with("cli-v") {
    rpm.global("tag", tag);
    if rpm.changed() {
      rpm.release();
      break;
    }
  }
}
