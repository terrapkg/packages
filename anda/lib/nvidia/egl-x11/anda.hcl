project pkg {
        arches = ["x86_64", "aarch64"]
    rpm {
        spec = "egl-x11.spec"
    }
    labels {
        subrepo = "nvidia"
        mock = 1
    }
}
