project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "ffmpeg.spec"
        extra_repos = ["https://repos.fyralabs.com/terrarawhide-nvidia", "https://repos.fyralabs.com/terrarawhide-multimedia"]
    }
    labels {
        updbranch = 1
        mock = 1
        subrepo = "multimedia"
    }
}
