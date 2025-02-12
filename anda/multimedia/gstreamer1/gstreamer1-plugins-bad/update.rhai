import "andax/bump_extras.rhai" as bump;

let bodhi_branch = bump::as_bodhi_ver(labels.branch);

let pkg = "gstreamer1-plugins-bad-free";
let branch = bump::as_bodhi_ver(labels.branch);

bump::follow_bodhi_vr(rpm, "gstreamer1-plugins-bad-free", branch);

let opencv_ver = bump::bodhi("opencv", bodhi_branch);
open_file("anda/multimedia/gstreamer1/gstreamer1-plugins-bad/OPENCV_VERSION.txt", "w").write(opencv_ver);
