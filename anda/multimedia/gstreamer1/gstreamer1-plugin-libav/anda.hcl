project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "gstreamer1-plugin-libav.spec"
        extra_repos = ["https://repos.fyralabs.com/terra\\$releasever-multimedia"]
    }
    labels {
        subrepo = "multimedia"
        mock = 1
        updbranch = 1
    }
}
