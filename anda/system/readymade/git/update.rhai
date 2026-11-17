import "andax/spec.rhai" as spec;

rpm.global("proc_macros_commit", gh_commit("FyraLabs/rdms_proc_macros"));
if rpm.changed() {
  let rel = spec::get_release(rpm).parse_int();
  rpm.release(rel + 1);
}

rpm.global("commit", gh_commit("FyraLabs/readymade"));
if rpm.changed() {
  rpm.release();
  rpm.global("commit_date", date());
}
