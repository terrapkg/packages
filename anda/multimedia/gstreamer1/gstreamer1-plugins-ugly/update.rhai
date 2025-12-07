import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

rpm.version(bump::alma("gstreamer1-plugins-ugly-free", "AppStream", labels.branch);

open_file("anda/multimedia/gstreamer1/gstreamer1-plugins-ugly/VERSION_x264.txt", "w").write(bump::madoguchi("x264", labels.branch));
open_file("anda/multimedia/gstreamer1/gstreamer1-plugins-ugly/VERSION_x265.txt", "w").write(bump::madoguchi("x265", labels.branch));

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
