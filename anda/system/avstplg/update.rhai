if filters.contains("nightly") {
  let req = new_req("https://api.github.com/repos/thesofproject/avsdk/commits/HEAD");
  req.head("Authorization", `Bearer ${env("GITHUB_TOKEN")}`);
  rpm.global("commit", json(req.get()).sha);
  rpm.release();
}