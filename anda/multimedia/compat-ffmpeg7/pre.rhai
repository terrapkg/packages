let key = get("https://ffmpeg.org/ffmpeg-devel.asc");
let dir = sub(`/[^/]+$`, "", __script_path);

open_file(`${dir}/ffmpeg-devel.asc`, "w").write(key);
sh(`gpg2 --import --import-options import-export,import-minimal ffmpeg-devel.asc > ./ffmpeg.keyring`, #{ "cwd": dir });
