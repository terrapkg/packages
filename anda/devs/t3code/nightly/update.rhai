rpm.global("commit", gh_commit("pingdotgg/t3code"));
if rpm.changed() {
  let ver = gh("pingdotgg/t3code");
  ver.crop(1);
  rpm.global("latest_stable_version", ver);
  rpm.release();
  rpm.global("commit_date", date());
}
