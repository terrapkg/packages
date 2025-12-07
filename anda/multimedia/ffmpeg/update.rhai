import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

// rpm.version(find(`<small>ffmpeg-([\d.]+?)\.tar\.xz</small>`, get("https://ffmpeg.org/download.html"), 1));
rpm.version(bump::bodhi("ffmpeg", bump::as_bodhi_ver(labels.branch)));

open_file("anda/multimedia/ffmpeg/VERSION_x264.txt", "w").write(bump::madoguchi("x264", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_x265.txt", "w").write(bump::madoguchi("x265", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_tesseract.txt", "w").write(bump::bodhi("tesseract", bump::as_bodhi_ver(labels.branch)));
open_file("anda/multimedia/ffmpeg/VERSION_rubberband.txt", "w").write(bump::bodhi("rubberband", bump::as_bodhi_ver(labels.branch)));
open_file("anda/multimedia/ffmpeg/VERSION_libbluray.txt", "w").write(bump::bodhi("libbluray", bump::as_bodhi_ver(labels.branch)));
open_file("anda/multimedia/ffmpeg/VERSION_libchromaprint.txt", "w").write(bump::bodhi("libchromaprint", bump::as_bodhi_ver(labels.branch)));
open_file("anda/multimedia/ffmpeg/VERSION_vvenc.txt", "w").write(bump::madoguchi("vvenc-libs", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_xeve.txt", "w").write(bump::madoguchi("xeve", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_xevd.txt", "w").write(bump::madoguchi("xevd", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_LCEVCdec.txt", "w").write(bump::madoguchi("LCEVCdec", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_svt-av1.txt", "w").write(bump::bodhi("svt-av1", bump::as_bodhi_ver(labels.branch)));

let dir = sub(`/[^/]+$`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
