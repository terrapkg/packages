project pkg {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "gstreamer1-plugin-libav.spec"
    }
    labels {
        subrepo = "multimedia"
        mock = 1
        updbranch = 1
    }
}
