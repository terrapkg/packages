rpm.version(gitlab_tag("44426042"));
if rpm.changed() {
  rpm.global("commit1", gitlab_commit("66855638", "main"));
}