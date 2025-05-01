project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    extra_repos = ["https://tetsudou.fyralabs.com/metalink?repo=terrarawhide-nvidia&arch=\\$basearch"]
    rpm {
        spec = "ffmpeg.spec"
    }
    labels {
        updbranch = 1
        mock = 1
    }
}
