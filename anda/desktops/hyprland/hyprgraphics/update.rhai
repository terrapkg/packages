import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

rpm.global("commit", gh_commit("hyprwm/hyprgraphics"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprgraphics", "main", "VERSION"));
	rpm.global("commit_date", date());
}

// FIXME: should be updbranch but we also need nightly and we are using gh_commit()?
let dir = sub(`/[^/]+$`, "", __script_path);
open_file(`${dir}/VER_hyprlang.txt`, "w").write(bump::madoguchi("hyprlang.nightly", labels.branch));
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
