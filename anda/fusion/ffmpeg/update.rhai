rpm.version(find(`<small>ffmpeg-([\d.]+?)\.tar\.xz</small>`, get("https://ffmpeg.org/download.html"), 1));
