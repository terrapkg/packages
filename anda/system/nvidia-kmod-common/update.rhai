let commit = get("https://api.github.com/repos/negativo17/nvidia-kmod-common/commits/HEAD").json().sha();
open_file("anda/system/nvidia-kmod-common/commit.txt").write(commit);
