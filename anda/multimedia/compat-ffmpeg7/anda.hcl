project pkg {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "compat-ffmpeg7.spec"
    }
    labels {
        updbranch = 1
        mock = 1
        subrepo = "multimedia"
    }
}
