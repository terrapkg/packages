rpm.global("commit", gh_commit("Milkshiift/GoofCord"));
 if rpm.changed() {
   let v = gh_tag("Milkshiift/GoofCord");
   v.crop(1);
   if `[\d.]+-beta\.\d+`.find_all(v).len == 0 {
     let v = sub(`-beta\.\d+`, "~", v);
     rpm.global("ver", v);
   } else {
   rpm.global("ver", v + `^`);
   }
   rpm.global("commit_date", date());
   rpm.release();
}
