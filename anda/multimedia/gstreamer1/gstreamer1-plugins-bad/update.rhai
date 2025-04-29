import "andax/bump_extras.rhai" as bump;

let bodhi_branch = bump::as_bodhi_ver(labels.branch);

let pkg = "gstreamer1-plugins-bad-free";
let branch = bump::as_bodhi_ver(labels.branch);

let vr = bump::bodhi_vr("gstreamer1-plugins-bad-free", branch);
rpm.version(vr[1]);
rpm.release(vr[2]);

let opencv_ver = bump::bodhi("opencv", bodhi_branch);
open_file("anda/multimedia/gstreamer1/gstreamer1-plugins-bad/OPENCV_VERSION.txt", "w").write(opencv_ver);
