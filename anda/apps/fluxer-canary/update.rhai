let r = new_req("https://api.github.com/repos/fluxerapp/fluxer/commits/canary");
r.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
rpm.global("commit", r.get().sha);
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
