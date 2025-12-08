project pkg {
    arches = ["x86_64", "aarch64"]
    rpm {
        spec = "ffmpeg.spec"
    }
    labels {
        updbranch = 1
        mock = 1
        subrepo = "multimedia"
    }
}
