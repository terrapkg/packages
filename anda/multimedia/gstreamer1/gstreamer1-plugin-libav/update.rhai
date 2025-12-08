import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

rpm.version(bump::bodhi("gstreamer1-plugin-libav", bump::as_bodhi_ver(labels.branch));

open_file("anda/multimedia/gstreamer1/gstreamer1-plugin-libav/VERSION_ffmpeg.txt", "w").write(bump::madoguchi("ffmpeg", labels.branch));

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
