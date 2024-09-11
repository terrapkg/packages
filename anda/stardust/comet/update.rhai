rpm.global("commit", gh_commit("StardustXR/comet"));
 if rpm.changed() {
   rpm.release();
   rpm.global("commit_date", date());
 }
