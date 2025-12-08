import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

// This doesn't currently exist in Alma but just in case
rpm.version(bump::alma("gstreamer1-vaapi", "AppStream", labels.branch));

open_file("anda/multimedia/gstreamer1/gstreamer1-vaapi/PLUGINS_BAD_release.txt", "w").write(bump::madoguchi_json("gstreamer1-plugins-bad", labels.branch).rel);

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
