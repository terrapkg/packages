project pkg {
    arches = ["x86_64"]
    rpm {
        spec = "gamescope-session-steam.spec"
    }
    labels {
        nightly = 1
    }
}
