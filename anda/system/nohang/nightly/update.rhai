import "andax/spec.rhai" as spec;

rpm.global("commit", gh_commit("hakavlad/nohang"));
if rpm.changed() {
  let rel = spec::get_release(rpm).parse_int();
  rpm.release(rel + 1);
}

rpm.global("ver", gh("hakavlad/nohang"));
