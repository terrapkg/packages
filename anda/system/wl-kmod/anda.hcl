project pkg {
    arches = ["x86_64", "i386"]
    rpm {
        spec = "wl-kmod.spec"
    }
    labels {
        mock = 1
    }
}
