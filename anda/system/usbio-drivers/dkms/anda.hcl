project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "dkms-intel-usbio.spec"
    }
    labels {
        updbranch = 1
    }
}
