import "andax/bump_extras.rhai" as bump;

rpm.version(find(`<small>ffmpeg-([\d.]+?)\.tar\.xz</small>`, get("https://ffmpeg.org/download.html"), 1));

let branch = labels.branch;
if branch.starts_with("f") {
	branch.crop(1); // remove the `f`
}

let ffmpeg_ver = get(`https://madoguchi.fyralabs.com/v4/terra${branch}/packages/x265`).json().ver;
open_file("anda/multimedia/ffmpeg/VERSION_x265.txt", "w").write(ffmpeg_ver);

let tesseract_ver = bump::bodhi("tesseract", bump::as_bodhi_ver(labels.branch));
open_file("anda/multimedia/ffmpeg/VERSION_tesseract.txt", "w").write(tesseract_ver);
