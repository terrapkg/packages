project pkg {
        arches = ["x86_64", "aarch64", "i386"]
    rpm {
        spec = "vvenc.spec"
    }
    labels {
        mock = 1
    }
}
