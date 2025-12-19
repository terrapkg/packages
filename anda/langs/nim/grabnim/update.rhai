import "andax/bump_extras.rhai" as bump;

rpm.global("commit", bump::codeberg_commit("janAkali/grabnim"));
if rpm.changed() {
    rpm.global("commit_date", date());
}
