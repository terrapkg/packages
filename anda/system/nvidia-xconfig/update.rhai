let commit = get("https://api.github.com/repos/negativo17/nvidia-xconfig/commits/HEAD").json().sha();
open_file("anda/system/nvidia-xconfig/commit.txt").write(commit);
