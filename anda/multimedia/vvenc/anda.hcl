project pkg {
        arches = ["x86_64", "aarch64"]
    rpm {
        spec = "vvenc.spec"
    }
    labels {
        mock = 1
        subrepo = "multimedia"
    }
}
