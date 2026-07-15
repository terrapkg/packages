rpm.global("ver", forgejo_tag("forgejo.ellis.link", "continuwuation/continuwuity"));
rpm.global("commit", forgejo_commit("forgejo.ellis.link", "continuwuation/continuwuity"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
