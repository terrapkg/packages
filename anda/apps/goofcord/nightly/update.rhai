rpm.global("commit", gh_commit("Milkshiift/GoofCord"));
 if rpm.changed {
   let v = gh_tag(""Milkshiift/GoofCord");
   v.crop(1);
   rpm.global("ver", v);
   rpm.global("commit_date", date());
   rpm.release();
}
