project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "intel-usbio-kmod.spec"
    }
    labels {
        mock = 1
        updbranch = 1
    }
}
