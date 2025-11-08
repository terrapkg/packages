project pkg {
        arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "vvdec.spec"
    }
    labels {
        mock = 1
    }
}
