let commit = get("https://api.github.com/repos/sharanda/manrope/commits/HEAD").json().sha();
open_file("andaq/system/nvidia-kmod-common").write(commit);
