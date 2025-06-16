project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "intel-usbio-drivers.spec"
    }
    labels {
        nightly = 1
    }
}
