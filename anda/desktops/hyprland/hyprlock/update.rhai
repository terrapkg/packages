import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

let v = gh_rawfile("hyprwm/hyprlock", "main", "VERSION");
v.trim();
rpm.version(v);

// FIXME: should be updbranch but we also need nightly and we are using gh_commit()?
let dir = sub(`/[^/]+$`, "", __script_path);
open_file(`${dir}/VER_hyprgraphics.txt`, "w").write(bump::madoguchi("hyprgraphics.nightly", labels.branch));
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
