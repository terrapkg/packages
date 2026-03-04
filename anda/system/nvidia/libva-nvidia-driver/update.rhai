rpm.global("commit0", gh_commit("elFarto/nvidia-vaapi-driver"));
if rpm.changed() {
  let v = gh("elFarto/nvidia-vaapi-driver");
  v.crop(1);
  v += "%{!?tag:^%{date}git%{shortcommit0}}";
  rpm.version(v);
  rpm.global("date", date());
}
