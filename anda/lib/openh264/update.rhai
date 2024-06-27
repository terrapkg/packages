rpm.global("commit1", gh_commit("mozilla/gmp-api"));
let h264 = gh("cisco/openh264");
h264.crop(1);
rpm.version(h264);
