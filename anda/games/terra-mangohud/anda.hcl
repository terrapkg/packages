project pkg {
    arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "terra-mangohud.spec"
    }
    labels {
        mock = 1
        subrepo = "extras"
    }
}
