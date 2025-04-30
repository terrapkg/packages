import "andax/bump_extras.rhai" as bump;

let vr = bump::bodhi_vr("gstreamer1-plugin-libav", bump::as_bodhi_ver(labels.branch));
rpm.version(vr[1]);
rpm.release(vr[2]);
