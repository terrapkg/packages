project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "gstreamer1-plugin-libav.spec"
    }
    labels {
        subrepo = "extras"
        mock = 1
        updbranch = 1
    }
}
