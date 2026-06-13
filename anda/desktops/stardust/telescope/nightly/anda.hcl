project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "stardust-telescope-nightly.spec"
    }
    labels {
        nightly = 1
    }
}
