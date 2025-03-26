rpm.global("commit", gh_commit("sonic2kk/steamtinkerlaunch"));
if rpm.changed() {
   rpm.release();
   rpm.global("commit_date", date());
   let v = gh("sonic2kk/steamtinkerlaunch");
   v.crop(1);
   rpm.global("ver", v);
}
