project pkg {
        arches = ["x86_64"]
    rpm {
        spec = "falcond-profiles.spec"
    }
    labels {
        nightly = 1
    }
}
