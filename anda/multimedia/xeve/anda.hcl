project pkg {
        arches = ["x86_64", "aarch64"]
    rpm {
        spec = "xeve.spec"
    }
    labels {
        mock = 1
        subrepo = "multimedia"
    }
}
