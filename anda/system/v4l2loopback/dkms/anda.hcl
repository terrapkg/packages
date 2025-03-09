project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "dkms-v4l2loopback.spec"
    }
    labels {
        mock = 1
        updbranch = 1
    }
}
