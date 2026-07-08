rpm.global("ver", get("https://forgejo.ellis.link/api/v1/repos/continuwuation/continuwuity/releases?pre-release=true").json().tag_name);
rpm.global("commit", forgejo_commit("forgejo.ellis.link", "continuwuation/continuwuity"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
