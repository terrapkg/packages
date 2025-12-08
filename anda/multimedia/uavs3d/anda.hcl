project pkg {
        arches = ["x86_64", "aarch64"]
    rpm {
        spec = "uavs3d.spec"
    }
    labels {
        mock = 1
        subrepo = "multimedia"
    }
}
