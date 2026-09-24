rpm.global("commit", gh_commit("openscad/openscad"));
if rpm.changed() {
  rpm.release();
  let v = gh("openscad/openscad");
  v.crop(9);
  rpm.global("latest_stable_version", v);
  rpm.global("commit_date", date());
}
