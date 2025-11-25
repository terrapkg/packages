import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

            // FIXME: should be updbranch but we also need nightly and we are using gh_commit()?
            let dir = sub(`/[^/]+$`, "", __script_path);
            open_file(`${dir}/VER_hyprutil.txt`, "w").write(bump::madoguchi("hyprutils.nightly", labels.branch));
            if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
                let rel = spec::get_release(rpm).parse_int();
                rpm.release(rel + 1);
            }

rpm.global("commit", gh_commit("hyprwm/hyprlang"));
if rpm.changed() {
	rpm.global("ver", gh_rawfile("hyprwm/hyprlang", "main", "VERSION"));
	rpm.global("commit_date", date());
}
