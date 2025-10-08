rpm.global("commit", gh_commit("WeirdTreeThing/croskbd"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
