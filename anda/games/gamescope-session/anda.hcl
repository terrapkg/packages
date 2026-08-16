project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "gamescope-session.spec"
    }
    labels {
        nightly = 1
    }
}
