import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

rpm.version(bump::alma("gstreamer1-plugins-bad-free", "AppStream", labels.branch));

open_file("anda/multimedia/gstreamer1/gstreamer1-plugins-bad/OPENCV_VERSION.txt", "w").write(bump::bodhi("opencv", bodhi_branch));
open_file("anda/multimedia/gstreamer1/gstreamer1-plugins-bad/LCEVCdec_VERSION.txt", "w").write(bump::madoguchi("LCEVCdec", labels.branch));
open_file("anda/multimedia/gstreamer1/gstreamer1-plugins-bad/OPENH264_VERSION.txt", "w").write(bump::madoguchi("openh264", labels.branch));

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
