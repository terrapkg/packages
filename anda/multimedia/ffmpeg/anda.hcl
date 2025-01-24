project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "ffmpeg.spec"
    }
    labels {
        updbranch = 1
        mock = 1
    }
}
