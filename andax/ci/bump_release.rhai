import "andax/spec.rhai" as spec;

let dir = sub(`/[^/]+`, "", __script_path);

if sh("[[ `git status " + dir + "--porcelain` ]] && exit 1", #{}).ctx.rc == 1 {
	spec::bump_release(rpm);
}
