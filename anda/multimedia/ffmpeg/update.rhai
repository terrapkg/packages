import "andax/bump_extras.rhai" as bump;
import "andax/spec.rhai" as spec;

rpm.version(find(`<small>ffmpeg-([\d.]+?)\.tar\.xz</small>`, get("https://ffmpeg.org/download.html"), 1));

open_file("anda/multimedia/ffmpeg/VERSION_x265.txt", "w").write(bump::madoguchi("x265", labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_tesseract.txt", "w").write(bump::bodhi("tesseract", bump::as_bodhi_ver(labels.branch)));
open_file("anda/multimedia/ffmpeg/VERSION_vvenc.txt", "w").write(bump::madoguchi("vvenc-libs", labels.branch));

let dir = sub(`/[^/]+`, "", __script_path);
if sh("[[ `git status " + dir + " --porcelain` ]] && exit 1 || exit 0", #{}).ctx.rc == 1 {
    let rel = spec::get_release(rpm).parse_int();
    rpm.release(rel + 1);
}
