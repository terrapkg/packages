let domain = `code.videolan.org`;
let c = gitlab_commit(domain, "536", "master");

rpm.global("commit", c);

if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
  rpm.global("api_version", find(`#define X264_BUILD ([\d]+)`, get(`https://${domain}/videolan/x264/-/raw/${c}/x264.h`), 1));
}
