project pkg {
        arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "egl-wayland.spec"
    }
    labels {
        subrepo = "nvidia"
        mock = 1
    }
}
