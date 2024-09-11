rpm.global("commit", gh_commit("StardustXR/protostar"));
 if rpm.changed() {
   rpm.release();
   rpm.global("commit_date", date());
 }
