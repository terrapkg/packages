project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "intel-ipu6-kmod.spec"
    }
    labels {
        mock = 1
    }
}
