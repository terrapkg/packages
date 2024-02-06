let commit = get("https://api.github.com/repos/sharanda/manrope/commits/HEAD").json().sha();
open_file("anda/system/nvidia-kmod-common/commit.txt").write(commit);
