project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "dkms-intel-ipu6.spec"
    }
    labels {
        mock = 1
        updbranch = 1
    }
}
