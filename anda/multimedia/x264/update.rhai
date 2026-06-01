let domain = `code.videolan.org`;
let c = gitlab_commit_domain(domain, "videolan/x264");

rpm.global("commit", c);

if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
  rpm.global("api_version", find(`#define X264_BUILD ([\d]+)`, get(`https://${domain}/videolan/x264/-/raw/${c}/x264.h`), 1));
}
