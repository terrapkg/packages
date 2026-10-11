project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "terra-xorg-x11-server-Xwayland.spec"
    }
    labels {
        mock = 1
        subrepo = "extras"
        updbranch = 1
    }
}
